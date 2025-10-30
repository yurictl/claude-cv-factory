#!/usr/bin/env python3
"""
Simple script to render CVs from cv-bank directory
"""
import os
import subprocess
import sys
from pathlib import Path

def render_cv(yaml_file):
    """Render a single CV file"""
    cv_bank_dir = Path("cv-bank")

    # Get the rendercv path from venv
    venv_rendercv = Path(__file__).parent / "venv" / "bin" / "rendercv"
    rendercv_cmd = str(venv_rendercv) if venv_rendercv.exists() else "rendercv"

    # Change to cv-bank directory
    original_dir = os.getcwd()
    os.chdir(cv_bank_dir)

    try:
        # Render the CV
        print(f"Rendering {yaml_file}...")
        result = subprocess.run([rendercv_cmd, "render", yaml_file],
                              capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error rendering {yaml_file}:")
            print(result.stdout)
            print(result.stderr)
            return False

        print(f"✅ Successfully rendered {yaml_file}")
        return True

    finally:
        os.chdir(original_dir)

def main():
    """Main function to render all CVs or a specific one"""
    if len(sys.argv) > 1:
        # Render specific CV
        yaml_file = sys.argv[1]
        if not yaml_file.endswith('.yaml'):
            yaml_file += '.yaml'
        
        if not Path(f"cv-bank/{yaml_file}").exists():
            print(f"Error: CV file {yaml_file} not found in cv-bank directory")
            sys.exit(1)
            
        success = render_cv(yaml_file)
        sys.exit(0 if success else 1)
    else:
        # Render all CVs in cv-bank directory
        cv_bank_dir = Path("cv-bank")
        yaml_files = list(cv_bank_dir.glob("*.yaml"))
        
        if not yaml_files:
            print("No YAML files found in cv-bank directory")
            sys.exit(1)
            
        print(f"Found {len(yaml_files)} CV files to render")
        
        success_count = 0
        for yaml_file in yaml_files:
            if render_cv(yaml_file.name):
                success_count += 1
                
        print(f"\nRendered {success_count}/{len(yaml_files)} CVs successfully")
        sys.exit(0 if success_count == len(yaml_files) else 1)

if __name__ == "__main__":
    main()
