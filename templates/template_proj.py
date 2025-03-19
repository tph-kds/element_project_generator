import yaml
from pathlib import Path
from typing import Dict, Any, List
from pydantic import BaseModel, Field


class ConfigOutput(BaseModel):
    message: str = Field(
        default="Hello from docs-pro!",
        description="The message to print the final result's status.",
    )
    succesed: bool = Field(
        default=True,
        description="The status of the final result.",
    )

class ProjectStructureGenerator:
    def __init__(self, config_path):
        super(ProjectStructureGenerator, self).__init__()
        self.config_path = Path(config_path)
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """
        Load the project structure configuration from the YAML file.

        Returns:
            dict: The project structure configuration.
        """
        try:
            with open(self.config_path, "r") as file:
                return yaml.safe_load(file)
            print(f"Successfully loaded config from {self.config_path}")
        except FileNotFoundError:
            print(f"Config file not found: {self.config_path}")
            return {}

    def generate(
            self, 
            target_dir: str = "./",
    ) -> ConfigOutput:
        """
        Generate the project structure based on the configuration and started from the target directory."
        
        Args:
            target_dir (str): The target directory where the project structure will be generated.

        Returns:
            noting: Successfully or Failedly generated from the target directory.
        """ 

        return self._create_project(
            target_path = Path(target_dir), 
            config = self.config
        )

    def _create_project(
            self, 
            target_path: Path, 
            config: Dict[str, Any]
    ) -> ConfigOutput:
        """
        Create the project structure based on the configuration.
        Args:
            target_path (Path): The target directory where the project structure will be generated.
            config (Dict[str, Any]): The project structure configuration.

        Returns:
            Dict[str, Any]: The project structure.
    
        """
        if config is None or not isinstance(config, dict):
            return ConfigOutput(
                message = f"Invalid config: {config}",
                succesed = False,
            )
        # # if existing directory is provided, clear all begin the main folder docs
        # if target_path.exists():
        #     for item in target_path.iterdir():
        #         if item.is_dir():
        #             item.rmdir()
        #         else:
        #             item.unlink()
        ## create a new directory project's strcuture 
        for name, content in config.items():
            item_path = target_path / name
            if isinstance(content, dict):
                # create dicrectory and recursively call _create_project
                item_path.mkdir(parents = True, exist_ok=True)
                self._create_project(item_path, content)
            else:
                # Create file and write content if provided
                item_path.parent.mkdir(parents=True, exist_ok=True)
                file_content = content if isinstance(content, str) else ""
                item_path.write_text(file_content)
        
        return ConfigOutput(
            message = f"Successfully created project structure in {target_path}",
            succesed = True,
        )


    def __repr__(self):
        return f"ProjectStructureGenerator(config_path='{self.config_path}')"
    



    

