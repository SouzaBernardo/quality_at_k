import os
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent


def create_dir(path):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

def save_file(path, content: str):
    with open(path, "w") as f:
        f.write(content)

def main():
    input_dir = PROJECT_ROOT / "classeval_quality" / "output"
    output_dir = PROJECT_ROOT / "classeval_quality" / "data"

    for file_name in os.listdir(input_dir):
        file_dir = input_dir / file_name
        for file_class in os.listdir(file_dir):
            output_save_dir = output_dir / file_name / file_class
            create_dir(output_save_dir)
            class_content_dir = file_dir / file_class / "filtered"
            for class_content in os.listdir(class_content_dir):
                content = open(class_content_dir / class_content, "r").read()
                save_file(output_save_dir / class_content, content)

                
                

if __name__ == "__main__":
    main()
        
