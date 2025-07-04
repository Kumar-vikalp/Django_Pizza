import os
import re

# Path to the site-packages of the broken virtual environment
site_packages_path = r"C:\Users\vikal\Downloads\Compressed\Django_Pizza\Django_Pizza\env\Lib\site-packages"

# Output file
output_file = "requirements.txt"

# Pattern to extract name and version
pattern = re.compile(r"^(.*?)-([\d\.]+)(\.dist-info|\.egg-info)$", re.IGNORECASE)

packages = []

for item in os.listdir(site_packages_path):
    match = pattern.match(item)
    if match:
        name, version = match.group(1), match.group(2)
        name = name.replace('_', '-')
        packages.append(f"{name}=={version}")

# Remove duplicates and sort
packages = sorted(set(packages))

# Save to requirements.txt
with open(output_file, "w") as f:
    f.write("\n".join(packages))

print(f"✅ Found {len(packages)} packages. Saved to {output_file}")
