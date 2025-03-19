from template_proj import ProjectStructureGenerator

if __name__ == "__main__":
    
    print(f"{__name__} is running from {__file__} to create project structure")
    
    psgen = ProjectStructureGenerator("templates/template.yaml")
    result = psgen.generate()
    print(f"Status of the final result: {result.succesed}")

    print(f"Successfully generated project structure from {__file__}")
