import json
import os
import shutil
def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)




data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """1""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Fall""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Neural Network Design Streamlit App """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The goal of this project is to convert all the Neural Network Deisgn Demos from Pyqt to streamlit.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            No Dataset is needed for this project .  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            This project is going to help students to use the book demos in web format and easier to access.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  
            
            1. Automate data capturing from Google Earth Engine (Python code in the engine).
            2. Work on the covariate features importance.  
            3. Use covariate features to model degree of poverty (Classical Models).
            4. Use a model developed in on city and apply it to other cities (Transfer Learning)
            5. Combine satellite images with covariate features.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  
            
            - (3 Weeks) Data Automation.  
            - (3 Weeks) Feature Importance  
            - (4 Weeks) Modeling  
            - (2 Weeks) Combine satellite images with covariate features  
            - (1 Weeks) Compiling Results  
            - (1 Weeks) Writing Up a paper and submission
            - (1 Weeks) Final Presentation  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            For this project maximum 4 students can work on it.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            The challenge is on data analysis part , find a good features and train a decent model.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Dr. Amir Jafari",
        "Proposed by email": "ajafari@gwu.edu",
        "instructor": "Amir Jafari",
        "instructor_email": "ajafari@gmail.com",
        "github_repo": "https://github.com/amir-jafari/Capstone",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(os.getcwd() + os.sep + f'Arxiv\Proposals\{data_to_save["Year"]}\{data_to_save["Semester"]}\{data_to_save["Version"]}',exist_ok=True)
output_file_path = os.getcwd() + os.sep + f'Arxiv\Proposals\{data_to_save["Year"]}\{data_to_save["Semester"]}\\{data_to_save["Version"]}\\'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy('json_gen.py',output_file_path )
print(f"Data saved to {output_file_path}")