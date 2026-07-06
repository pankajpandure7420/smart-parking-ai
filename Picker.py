import cv2
import pickle
import os

# Slot chi size (Video nusar standard size)
width, height = 107, 48 

# Jar aadhi slots save asatil tar te load kara
if os.path.exists('CarParkPos'):
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
else:
    posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
        print(f"Slot add kela: {x}, {y}")
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
                print("Slot kadhla")
    
    # Pratyek click nantar file save kara
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread('carParkImg.png')
    if img is None:
        print("❌ Error: 'carParkImg.png' sapdat nahiye! Folder baha.")
        break

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Parking Picker - Mark Slots & Press Q", img)
    cv2.setMouseCallback("Parking Picker - Mark Slots & Press Q", mouseClick)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(f"✅ Total {len(posList)} slots save jhale ahet!")
        break

cv2.destroyAllWindows()