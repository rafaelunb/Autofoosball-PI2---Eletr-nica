import json
import base64
from ttdraw import _DRAW
from ttcontrol import _CONTROL

def StatusUpdateEvent():
    global Totron64,yGOL,aGOL,yDEF,aDEF,yMEI,aMEI,yATA,aATA
    _StatusUpdateEvent={"evenType": "status_update",
                        "camera": {"image": Totron64},
                         "lanes":[{"laneID": 0,"currentPosition": yGOL,"rotation": aGOL},
                                  {"laneID": 1,"currentPosition": yDEF,"rotation": aDEF},
                                  {"laneID": 2,"currentPosition": yMEI,"rotation": aMEI},
                                  {"laneID": 3,"currentPosition": yATA,"rotation": aATA}]}    
                                 
    return json.dumps(_StatusUpdateEvent)

def RegisterEvent():
    _RegisterEvent ={"evenType": "register",
                     "fieldDefinition": {"dimensions": [116, 77], # comprimento e largura em cm
                                         "lanes": [ {"laneID": 0,"xPosition":  7.0,"playerCount": 1,"playerDistance": 25.0,"movementLimit": 12.5},
                                                    {"laneID": 1,"xPosition": 71.5,"playerCount": 2,"playerDistance": 25.0,"movementLimit": 13.5},
                                                    {"laneID": 2,"xPosition": 50.5,"playerCount": 5,"playerDistance": 12.8,"movementLimit":  6.0},
                                                    {"laneID": 3,"xPosition": 79.5,"playerCount": 3,"playerDistance": 16.3,"movementLimit": 12.0}]},
                     "cameraSettings": {"framerate": 60,
                                        "resolution": [int, int]}} # comprimento e largura em pixels
    return json.dumps(str(_RegisterEvent))



print("Register Event: ")
print(RegisterEvent())
while True:
    global Totron64,yGOL,aGOL,yDEF,aDEF,yMEI,aMEI,yATA,aATA
    
    ActionEvent = input("Action Event: ")                          #{"evenType":"action", "desiredState":{"laneID":1,"position":10.5,"kick":"True"}}
    A = json.loads(ActionEvent)["desiredState"]
    
    [yGOL,aGOL,yDEF,aDEF,yMEI,aMEI,yATA,aATA] = _CONTROL(A["laneID"],-A["position"],A["kick"])
    '''
    raspistill -t 2000 -o Totron.jpg -n -w wResol -h hResol #Frame em .jpg
    with open("Totron.jpg", "rb") as image_file:
        Totron64 = base64.b64encode(image_file.read())      #Frame em Base64
    ''' 
    Totron64 = "imagem_base_64"
    print("Status Update Event: ")
    print(StatusUpdateEvent())