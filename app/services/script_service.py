from typing import List, Optional
from models.script_model import Script
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime


class ScriptService:
    def create_script(self, script: Script, db: Session) -> Script:
        # Basic validation
        if not all([script.name, script.language, script.script_content]):
            raise ValueError("Name, language, and script_content are required")

        try:
            db.add(script)
            db.commit()
            db.refresh(script)
            return script
        except IntegrityError:
            db.rollback()
            raise ValueError(f"Script '{script.name}' already exists")

    def get_script_by_name(self, name: str, db: Session) -> Optional[Script]:
        return db.query(Script).filter(Script.name == name).first()

    def search_scripts(
        self, name: Optional[str], language: Optional[str]
    ) -> List[Script]:
        pass

    def get_script_by_language(self, language: str) -> Optional[Script]:
        # Your business logic here
        pass

    def get_all_scripts(self) -> List[Script]:
        # Your business logic here
        pass

    def update_script(self, name: str, script: Script) -> Script:
        # Your business logic here
        pass

    def delete_script_by_name(self, name: str) -> None:
        # Your business logic here
        pass
