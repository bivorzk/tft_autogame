import cv2
import numpy as np
import pyautogui as pg
import win32api, win32con, win32gui, win32com.client
import time
import path as p
import os


play = cv2.imread("images/Play_Button.png", cv2.IMREAD_UNCHANGED)
if play is None:
    raise FileNotFoundError("Play_Button.png doesn't exist.")
if play.shape[2] == 4:
    # RGBA to RGB
    play = cv2.cvtColor(play, cv2.COLOR_BGRA2BGR)
play_gray = cv2.cvtColor(play, cv2.COLOR_BGR2GRAY)

coopvsai = cv2.imread("images/CoopVsAI.png", cv2.IMREAD_UNCHANGED)
if coopvsai is None:
    raise FileNotFoundError("CoopVsAI.png doesn't exist.")
if coopvsai.shape[2] == 4:
    # RGBA to RGB
    coopvsai = cv2.cvtColor(coopvsai, cv2.COLOR_BGRA2BGR)
coopvsai_gray = cv2.cvtColor(coopvsai, cv2.COLOR_BGR2GRAY)

tft = cv2.imread("images/TFT.png", cv2.IMREAD_UNCHANGED)
if tft is None:
    raise FileNotFoundError("TFT.png doesn't exist.")
if tft.shape[2] == 4:
    # RGBA to RGB
    tft = cv2.cvtColor(tft, cv2.COLOR_BGRA2BGR)
tft_gray = cv2.cvtColor(tft, cv2.COLOR_BGR2GRAY)



selectMode = cv2.imread("images/confirm.png", cv2.IMREAD_UNCHANGED)
if selectMode is None:
    raise FileNotFoundError("Confirm.png doesn't exist.")
if selectMode.shape[2] == 4:
    # RGBA to RGB
    selectMode = cv2.cvtColor(selectMode, cv2.COLOR_BGRA2BGR)
selectMode_gray = cv2.cvtColor(selectMode, cv2.COLOR_BGR2GRAY)


normal = cv2.imread("images/normal_game.png", cv2.IMREAD_UNCHANGED)
if normal is None:
    raise FileNotFoundError("Normal_Game.png doesn't exist.")
if normal.shape[2] == 4:
    # RGBA to RGB
    normal = cv2.cvtColor(normal, cv2.COLOR_BGRA2BGR)
normal_gray = cv2.cvtColor(normal, cv2.COLOR_BGR2GRAY)


findMatch = cv2.imread("images/find_match.png", cv2.IMREAD_UNCHANGED)
if findMatch is None:
    raise FileNotFoundError("FindMatch.png doesn't exist.")
if findMatch.shape[2] == 4:
    # RGBA to RGB
    findMatch = cv2.cvtColor(findMatch, cv2.COLOR_BGRA2BGR)
findMatch_gray = cv2.cvtColor(findMatch, cv2.COLOR_BGR2GRAY)


AcceptGame = cv2.imread("images/accept.png", cv2.IMREAD_UNCHANGED)
if AcceptGame is None:
    raise FileNotFoundError("Accept.png doesn't exist.")
if AcceptGame.shape[2] == 4:
    # RGBA to RGB
    AcceptGame = cv2.cvtColor(AcceptGame, cv2.COLOR_BGRA2BGR)
AcceptGame_gray = cv2.cvtColor(AcceptGame, cv2.COLOR_BGR2GRAY)


confirm2 = cv2.imread("images/confirm2.png", cv2.IMREAD_UNCHANGED)
if confirm2 is None:
    raise FileNotFoundError("confirm2.png doesn't exist.")
if confirm2.shape[2] == 4:
    # RGBA to RGB
    confirm2 = cv2.cvtColor(confirm2, cv2.COLOR_BGRA2BGR)
confirm2_gray = cv2.cvtColor(confirm2, cv2.COLOR_BGR2GRAY)


PickSion = cv2.imread("images/Sion.png", cv2.IMREAD_UNCHANGED)
if PickSion is None:
    raise FileNotFoundError("Sion.png doesn't exist.")
if PickSion.shape[2] == 4:
    # RGBA to RGB
    PickSion = cv2.cvtColor(PickSion, cv2.COLOR_BGRA2BGR)
PickSion_gray = cv2.cvtColor(PickSion, cv2.COLOR_BGR2GRAY)


lockin = cv2.imread("images/LOCK_IN.png", cv2.IMREAD_UNCHANGED)
if lockin is None:
    raise FileNotFoundError("LOCK_IN.png doesn't exist.")
if lockin.shape[2] == 4:
    # RGBA to RGB
    lockin = cv2.cvtColor(lockin, cv2.COLOR_BGRA2BGR)
lockin_gray = cv2.cvtColor(lockin, cv2.COLOR_BGR2GRAY)

while True:
    screen = pg.screenshot()
    screen_np = np.array(screen)
    if screen_np.shape[2] == 4:
        screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
    # Step 1: Click Play button
    result_play = cv2.matchTemplate(screen_gray, play_gray, cv2.TM_CCOEFF_NORMED)
    loc_play = np.where(result_play >= 0.7)
    if len(loc_play[0]) > 0:
        y, x = loc_play[0][0], loc_play[1][0]
        win32api.SetCursorPos((x + play.shape[1] // 2, y + play.shape[0] // 2))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(2)

        # Click TFT button
        while True:
            screen = pg.screenshot()
            screen_np = np.array(screen)
            if screen_np.shape[2] == 4:
                screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
            screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
            screen_gray = screen_gray.astype(np.uint8)
            result_tft = cv2.matchTemplate(screen_gray, tft_gray, cv2.TM_CCOEFF_NORMED)
            loc_tft = np.where(result_tft >= 0.7)
            if len(loc_tft[0]) > 0:
                y, x = loc_tft[0][0], loc_tft[1][0]
                win32api.SetCursorPos((x + tft.shape[1] // 2, y + tft.shape[0] // 2))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                time.sleep(2)
                break
            time.sleep(2)
        # Apply selected mode
        while True:
            screen = pg.screenshot()
            screen_np = np.array(screen)
            if screen_np.shape[2] == 4:
                screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
            screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
            screen_gray = screen_gray.astype(np.uint8)
            result_normal = cv2.matchTemplate(screen_gray, normal_gray, cv2.TM_CCOEFF_NORMED)
            loc_normal = np.where(result_normal >= 0.6)
            if len(loc_normal[0]) > 0:
                y, x = loc_normal[0][0], loc_normal[1][0]
                win32api.SetCursorPos((x + normal.shape[1] // 2, y + normal.shape[0] // 2))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                time.sleep(2)
                break
            time.sleep(2)
        # Confirm selection
        while True:
            screen = pg.screenshot()
            screen_np = np.array(screen)
            if screen_np.shape[2] == 4:
                screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
            screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
            screen_gray = screen_gray.astype(np.uint8)
            result_confirm2 = cv2.matchTemplate(screen_gray, confirm2_gray, cv2.TM_CCOEFF_NORMED)
            loc_confirm2 = np.where(result_confirm2 >= 0.65)
            if len(loc_confirm2[0]) > 0:
                y, x = loc_confirm2[0][0], loc_confirm2[1][0]
                win32api.SetCursorPos((x + confirm2.shape[1] // 2, y + confirm2.shape[0] // 2))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                time.sleep(2)
                break
            time.sleep(3.5)
        # Click normal game
        # Find Match button
     #   print("test")
    time.sleep(8)
    while True:
        print("----------------------------------------")
        screen = pg.screenshot() 
        screen_np = np.array(screen)
        if screen_np.shape[2] == 4:
            screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
        screen_gray = screen_gray.astype(np.uint8)
        result_find = cv2.matchTemplate(screen_gray, findMatch_gray, cv2.TM_CCOEFF_NORMED)
        print(np.max(result_find))
        loc_find = np.where(result_find >= 0.6)
        if len(loc_find[0]) > 0:
            y, x = loc_find[0][0], loc_find[1][0]
            win32api.SetCursorPos((x + findMatch.shape[1] // 2, y + findMatch.shape[0] // 2))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            break
    # Accept Game button
    while True:
        screen = pg.screenshot()
        screen_np = np.array(screen)
        if screen_np.shape[2] == 4:
            screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
        screen_gray = screen_gray.astype(np.uint8)
        result_accept = cv2.matchTemplate(screen_gray, AcceptGame_gray, cv2.TM_CCOEFF_NORMED)
        loc_accept = np.where(result_accept >= 0.65)
        if len(loc_accept[0]) > 0:
            #y, x = loc_accept[0][0], loc_accept[1][0]
            for i in range(10):
                print("Found!")
            #win32api.SetCursorPos((x + AcceptGame.shape[1] // 2, y + AcceptGame.shape[0] // 2))
            #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(2)
            break
        time.sleep(5)

    # Champ Select Implementation Here ---------------------

    


 