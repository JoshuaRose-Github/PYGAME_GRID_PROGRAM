try:
    import pygame
    import random
    import math
    import string
    import re
    import psutil
    import sys
    import os
    import getpass
    import openpyxl
    import threading
except ImportError as Error:
    print(f"There was an error whilst importing 1 or more modules."+"\n"+f"Error: {str(Error)}")

__user__   = getpass.getuser()
__author__ = "__JoshuaRose__"

class SocketWindow:

    def __init__(self, window_width, window_height, caption):

        # COLORS
        self.GREY = (211,211,211)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)

        self.caption = caption
        self.GRID_STATUS = -1

        self.window_height = window_height
        self.window_width = window_width
        self.display_modes = None
        self.clock = pygame.time.Clock()

        self.running = 1

        # ONLY ONCE


        self.WINDOW = pygame.display.set_mode((window_width, window_height), pygame.DOUBLEBUF)
        self.FPS = 60

        CLASS_THREAD_EVENT_LOOP = threading.Thread(target=self.EVENT_LOOP)

        self.WINDOW.fill(self.WHITE)

        CLASS_THREAD_GREY_WINDOW = threading.Thread(target=self.GREY_WINDOW)

        CLASS_THREAD_GREY_WINDOW.daemon = True
        CLASS_THREAD_EVENT_LOOP.daemon = True

        #CLASS_THREAD_FPS_WINDOW.start()
        #CLASS_THREAD_EVENT_LOOP.start()


        # START EVENT LOOP WITHOUT THREAD
        self.EVENT_LOOP()

    def GRID_A(self):

        count_interval_a = 0
        count_interval_b = 0

        for i in range(100):
            self.GREY_WINDOW(1, 400, count_interval_a,0)
            count_interval_a += 4



        for i in range(100):
            self.GREY_WINDOW(400, 1, 0,count_interval_b)
            count_interval_b += 4

    def GRID_B(self):

        count_interval_a = 0
        count_interval_b = 0

        for i in range(100):
            self.GREY_WINDOW(2, 400, count_interval_a,0)
            count_interval_a += 6



        for i in range(100):
            self.GREY_WINDOW(400, 2, 0,count_interval_b)
            count_interval_b += 6

    def GRID_C(self):

        count_interval_a = 0
        count_interval_b = 0

        for i in range(100):
            self.GREY_WINDOW(3, 400, count_interval_a,0)
            count_interval_a += 8



        for i in range(100):
            self.GREY_WINDOW(400, 3, 0,count_interval_b)
            count_interval_b += 8

    def GRID_D(self):

        count_interval_a = 0
        count_interval_b = 0

        for i in range(100):
            self.GREY_WINDOW(4, 400, count_interval_a,0)
            count_interval_a += 10



        for i in range(100):
            self.GREY_WINDOW(400, 4, 0,count_interval_b)
            count_interval_b += 10

    def GRID_E(self):

        count_interval_a = 0
        count_interval_b = 0

        for i in range(100):
            self.GREY_WINDOW(5, 400, count_interval_a,0)
            count_interval_a += 12



        for i in range(100):
            self.GREY_WINDOW(400, 5, 0,count_interval_b)
            count_interval_b += 12

    def GRID_F(self):

        count_interval_a = 0
        count_interval_b = 0

        for i in range(100):
            self.GREY_WINDOW(6, 400, count_interval_a,0)
            count_interval_a += 14



        for i in range(100):
            self.GREY_WINDOW(400, 6, 0,count_interval_b)
            count_interval_b += 14





    def WIPE_SCREEN(self,color):
        self.WINDOW.fill(color)

    def GREY_WINDOW(self, fps_window_surf_width, fps_window_surf_height, cor_x,cor_y):

        BOX_TRANSPARENCY = 500

        FPS_WINDOW_BACK_RECT = pygame.Surface((fps_window_surf_width, fps_window_surf_height))

        FPS_WINDOW_BACK_RECT.set_alpha(BOX_TRANSPARENCY)

        FPS_WINDOW_BACK_RECT.fill(self.GREY)

        self.WINDOW.blit(FPS_WINDOW_BACK_RECT, (cor_x,cor_y))




    def EVENT_LOOP(self):



        while self.running:




            # self.GREY_WINDOW(400, 20,0,0)

            pygame.display.set_caption(self.caption)

            self.clock.tick(self.FPS)

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.running -= 1

                if ev.type == pygame.KEYDOWN:
                    print("CHANGING GRID")
                    if ev.key == pygame.K_SPACE:


                        self.GRID_STATUS += 1


                        if self.GRID_STATUS == 0:
                            self.WIPE_SCREEN(self.WHITE)
                            self.GRID_A()
                            pass
                        if self.GRID_STATUS == 1:
                            self.WIPE_SCREEN(self.WHITE)
                            self.GRID_B()

                        if self.GRID_STATUS == 2:
                            self.WIPE_SCREEN(self.WHITE)
                            self.GRID_C()

                        if self.GRID_STATUS == 3:
                            self.WIPE_SCREEN(self.WHITE)
                            self.GRID_D()

                        if self.GRID_STATUS == 4:
                            self.WIPE_SCREEN(self.WHITE)
                            self.GRID_E()

                        if self.GRID_STATUS == 5:
                            self.WIPE_SCREEN(self.WHITE)
                            self.GRID_F()

                    # if ev.type == pygame.KEYDOWN:
                    #     # KEYPRESS
                    #     if ev.type == pygame.K_ESCAPE:
                    #         pygame.exit()

            pygame.display.flip()




MainClassObject = SocketWindow(400, 400, "Beta 1.1.1")

# MainClassObject.EVENT_LOOP()