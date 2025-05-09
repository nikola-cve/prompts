import os
import yaml

# Folder containing the .md files
PROMPTS_FOLDER = "prompts"
OUTPUT_FILE = "prompts.yaml"

def read_md_files(folder):
    """Reads all .md files in the folder and extracts their content."""
    prompts = []
    for filename in os.listdir(folder):
        if filename.endswith(".md"):
            filepath = os.path.join(folder, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                prompts.append({
                    "filename": filename,
                    "content": content.strip()
                })
    return prompts

def write_yaml_file(data, output_file):
    """Writes the given data to a YAML file."""
    with open(output_file, "w", encoding="utf-8") as file:
        yaml.dump(data, file, allow_unicode=True, default_flow_style=False)
    print(f"Generated {output_file} successfully!")

if __name__ == "__main__":
    # Ensure the prompts folder exists
    if not os.path.exists(PROMPTS_FOLDER):
        print(f"Error: Folder '{PROMPTS_FOLDER}' not found!")
        exit(1)
    
    # Read .md files and generate YAML
    prompts_data = read_md_files(PROMPTS_FOLDER)
    write_yaml_file(prompts_data, OUTPUT_FILE)