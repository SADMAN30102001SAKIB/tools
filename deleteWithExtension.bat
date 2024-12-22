@echo off
set "folder_path=D:\Courses\MobileDev\Udemy - React Native - The Practical Guide 2023"
set "extension=.srt"

for /r "%folder_path%" %%F in (*%extension%) do (
    echo Deleting "%%F"
    del "%%F"
)

echo All files with the extension %extension% have been deleted.
