@echo off
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate

rem Ensure base folder structure
for %%d in (src scripts docs config) do (
    if not exist %%d (
        mkdir %%d
    )
)

pip install -r requirements.txt
