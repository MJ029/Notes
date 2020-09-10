ECHO OFF
SET ENV_NAME=%1
ECHO Setting up Jupyter Notebook on %ENV_NAME% environment

SET root=%userprofile%\anaconda3

CALL %root%/Scripts/activate.bat %ENV_NAME%
python -m ipykernel install --user --name=%ENV_NAME%