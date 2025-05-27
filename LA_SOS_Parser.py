import re
import csv

input_file = r"file_path.txt"
output_file = r"file_path.csv"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

entries = []
entry = {}
officers = []

for line in lines:
    line = line.strip()

    # New business entry
    match = re.match(r"^(\d{8}[A-Z])\s+(\d{1,2}/\d{1,2}/\d{4})\s+(.*?)\s{2,}(.*?)$", line)
    if match:
        if entry:
            # Add officers to columns
            for i, (name, address) in enumerate(officers[:5], 1):
                entry[f"Officer {i} Name"] = name
                entry[f"Officer {i} Address"] = address
            entries.append(entry)
            entry = {}
            officers = []

        entry["Filing Number"] = match.group(1)
        entry["Filing Date"] = match.group(2)
        entry["Business Name"] = match.group(3).strip()
        entry["Business Address"] = match.group(4).strip()

    elif line.startswith("Agent:"):
        agent_match = re.match(r"Agent:\s+(.*?)\s{2,}(.*)", line)
        if agent_match:
            entry["Agent Name"] = agent_match.group(1).strip()
            entry["Agent Address"] = agent_match.group(2).strip()

    elif "Officer:" in line or "Member/Manager:" in line:
        officer_match = re.match(r"(?:Officer:|Member/Manager:)\s+(.*?)\s{2,}(.*)", line)
        if officer_match:
            name = officer_match.group(1).strip()
            address = officer_match.group(2).strip()
            officers.append((name, address))

# Add final entry
if entry:
    for i, (name, address) in enumerate(officers[:5], 1):
        entry[f"Officer {i} Name"] = name
        entry[f"Officer {i} Address"] = address
    entries.append(entry)

# Gather all possible column names
base_fields = [
    "Filing Number", "Filing Date", "Business Name", "Business Address",
    "Agent Name", "Agent Address"
]
officer_fields = [f"Officer {i} Name" for i in range(1, 6)] + [f"Officer {i} Address" for i in range(1, 6)]
fieldnames = base_fields + officer_fields

# Write to CSV
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(entries)

print(f"Parsing complete. Data saved to: {output_file}")
