# Generating Project Structure

## Introduction
This guide explains how to use the `ProjectStructureGenerator` to generate a project structure based on a YAML configuration file.

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `pyyaml` for parsing YAML files
- `pydantic` for structured validation

To install dependencies, run:
```bash
pip install pyyaml pydantic
```

## Steps to Generate a Project Structure

### 1. Create a YAML Configuration File
Define the project structure in a `.yaml` file. Example:
```yaml
docs:
  docs:
    about:
      license.md: ""
    config:
        ...
  themse_overrides:
    main.html: ""
  Makefile: ""
  mkdocs.yaml: ""
  local.yaml: ""
  README.md: "# Project Documentation"  # Readme file

```

### 2. Use `ProjectStructureGenerator`
Write a Python script to generate the structure:
```python
from template_proj import ProjectStructureGenerator

generator = ProjectStructureGenerator("config.yaml")
output = generator.generate(target_dir="./output")
print(output.message)
```

### 3. Run the Script
Execute the script:
```bash
python templates/main.py
```
Or, if you have used uv library for sync this project
```bash
uv run templates/main.py
```

### 4. Check the Output
If successful, you should see:
```bash
Status of the final result: True
Successfully generated project structure from "./"
```
Your project structure will be generated based on the YAML file.

## Conclusion
Using `ProjectStructureGenerator`, you can quickly set up predefined project structures, ensuring consistency across different projects.

