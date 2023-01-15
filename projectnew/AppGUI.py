import PySimpleGUI as sg
import os.path
from Controler import Controler

class AppGUI:
    def __init__(self):
        fileListLayout = [
            [
                sg.Text("Image Folder"),
                sg.In(size=(25, 1), enable_events=True, key="FOLDER"),
                sg.FolderBrowse(),
            ],
            [
                sg.Listbox(
                    values=[[]], enable_events=True, size=(40, 20), key="FILE LIST"
                )
            ],[
                sg.Listbox(
                    values=[[]], enable_events=True, size=(40, 20), key="CLUSER LIST"
                )
            ],
        ]
        imageDisplayLayout = [
            [sg.Text("Choose an image from list on left:")],
            [sg.Text(size=(40, 1), key="PATH")],
            [sg.Image(key="IMAGE")],
        ]

        # ----- Final layout -----
        layout = [
            [
                sg.Column(fileListLayout),
                sg.VSeperator(),
                sg.Column(imageDisplayLayout),
            ]
        ]
        self.fileList = []

        window = sg.Window("Image Viewer", layout)
        self.runApp(window)

    def runApp(self, window):
        # Run the Event Loop
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            # Folder name was filled in, make a list of files in the folder
            if event == "FOLDER":
                folder = values["FOLDER"]
                try:
                    # Get list of files in folder
                    self.fileList = os.listdir(folder)
                    print(self.fileList)
                    print(folder)
                    controler = Controler(folder)
                    controler.runAlgorith()
                    #print(controler.returnCluster(1))
                    #print(controler.returnAllClusters())
                except:
                    self.fileList = []

                fileNames = [
                    f
                    for f in self.fileList
                    if os.path.isfile(os.path.join(folder, f))
                       and f.lower().endswith((".png", ".gif"))
                ]
                window["FILE LIST"].update(fileNames)
            elif event == "FILE LIST":  # A file was chosen from the listbox
                try:
                    newFileName = os.path.join(
                        values["FOLDER"], values["FILE LIST"][0]
                    )
                    window["PATH"].update(newFileName)
                    window["IMAGE"].update(filename=newFileName)
                except:
                    pass
        window.close()