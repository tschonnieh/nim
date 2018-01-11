import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as manimation
from q_learning.Rewards import Rewards

class Logger():
    def __init__(self, episodes_per_epoch):
        self.step_size = 0
        self.unknown_states = []
        self.lost_states = []
        self.vis_init = True
        self.episodes_per_epoch = episodes_per_epoch

    def initVis(self):
        if self.vis_init:
            self.init_video_writer('test.mp4')

    def stepEpoch(self, unknown_states, lost_states):
        self.unknown_states.append(unknown_states)
        self.lost_states.append(lost_states)

    def showPlot(self):
        #plt.plot(self.unknown_states, 'r')
        #plt.plot(self.lost_states, 'g')
        #plt.show()

        fig, ax1 = plt.subplots()
        x = np.arange(0, len(self.unknown_states))
        ax1.plot(x, self.unknown_states, 'b-')
        ax1.set_xlabel('Epochs (x' + str(self.episodes_per_epoch) + ')')
        ax1.set_ylabel('Unknown States', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(x, self.lost_states, 'r-')
        ax2.set_ylabel('Lost in beginning states', color='r')
        ax2.tick_params('y', colors='r')

        fig.tight_layout()
        plt.show()

    def init_video_writer(self, path_to_video):
        self.fig = plt.figure()
        FFMpegWriter = manimation.writers['ffmpeg']
        self.writer = FFMpegWriter(fps=15)
        self.writer.setup(self.fig, path_to_video, dpi=300)

    def finish_video_writer(self):
        self.writer.finish()

    def vis(self, qTable):
        table_size = qTable.shape
        img = np.zeros(table_size + (3,))

        # Invalid
        mask = qTable == Rewards['Invalid']
        img[mask, 0] = 0.0
        img[mask, 1] = 0.0
        img[mask, 2] = 1.0

        # Positiv Q-Value
        mask = qTable > 0
        img[mask, 0] = 0.0
        img[mask, 1] = 1.0
        img[mask, 2] = 0.0

        # Negativ Q-Value
        mask = qTable < 0
        mask *= qTable > Rewards['Invalid']
        img[mask, 0] = 1.0
        img[mask, 1] = 0.0
        img[mask, 2] = 0.0

        if self.vis_init:
            self.plot = plt.imshow(img)
            plt.axis("off")
            plt.pause(0.001)
            self.vis_init = False
        else:
            self.plot.set_data(img)
            plt.pause(0.001)

        if hasattr(self, 'writer'):
            self.writer.grab_frame()
