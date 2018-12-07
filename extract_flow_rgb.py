import numpy as np
import os

root_path = "/home/gavin/Downloads/UCF-101"
flow_path = "/home/gavin/Dataset/UCF-101_Flow"

# ./denseFlow -f /home/gavin/Downloads/UCF-101/ApplyEyeMakeup/v_ApplyEyeMakeup_g01_c01.avi
# -x /home/gavin/Dataset/UCF-101_Flow/ApplyEyeMakeup/v_ApplyEyeMakeup_g01_c01/x
# -y /home/gavin/Dataset/UCF-101_Flow/ApplyEyeMakeup/v_ApplyEyeMakeup_g01_c01/y
# -i /home/gavin/Dataset/UCF-101_Flow/ApplyEyeMakeup/v_ApplyEyeMakeup_g01_c01/i -b 20

def extract_flow_rgb(root_dirs):
    video_dirs = os.listdir(root_dirs) # ApplyEyeMakeup,...
    for video_dir in video_dirs:
        tmp = video_dir
        video_dir = os.path.join(root_dirs, video_dir) # root_path/ApplyEyeMakeup
        flow_dir = os.path.join(flow_path, tmp) # flow_path/ApplyEyeMakeup
        video_list = os.listdir(video_dir) # v_ApplyEyeMakeup_g01_c01.avi,...
        for video in video_list:
            video_name = video.split('.')[0]
            # tmp_dir = os.path.join(video_dir, video_name)
            tmpFlow_dir = os.path.join(flow_dir, video_name)
            tmp_file = os.path.join(video_dir, video)
            print(tmp_file) # path/UCF-101/ApplyEyeMakeup/v_ApplyEyeMakeup_g01_c01.avi

            if not os.path.exists(tmpFlow_dir):
                os.makedirs(tmpFlow_dir)

            i_dir = os.path.join(tmpFlow_dir,'i')
            x_dir = os.path.join(tmpFlow_dir, 'x')
            y_dir = os.path.join(tmpFlow_dir, 'y')

            cmd = './denseFlow -f %s -x %s -y %s -i %s -b 20' % (tmp_file,x_dir,y_dir,i_dir)
            if len(tmp_file.split('.')) > 1:
                os.system(cmd)
                print("extract rgb and flow from %s done." % (video))


def splitflow(root_dirs):
    video_dirs = os.listdir(root_dirs)
    for video_dir in video_dirs:
        tmp = video_dir
        video_dir = os.path.join(root_dirs, video_dir)
        video_list = os.listdir(video_dir)
        for video in video_list:
            print(os.path.join(video_dir, video))
            image_list = os.listdir(os.path.join(video_dir, video))
            i_dir = os.path.join(video_dir, video, 'i')
            x_dir = os.path.join(video_dir, video, 'x')
            y_dir = os.path.join(video_dir, video, 'y')
            if not os.path.exists(i_dir):
                os.makedirs(i_dir)
            if not os.path.exists(x_dir):
                os.makedirs(x_dir)
            if not os.path.exists(y_dir):
                os.makedirs(y_dir)
            for image in image_list:
                classic = image.split('_')[0]
                cmd = 'mv %s %s' % (os.path.join(video_dir, video, image), os.path.join(video_dir, video, classic))
                if len(image.split('_')) > 1:
                    os.system(cmd)


if __name__ == '__main__':
    extract_flow_rgb(root_path)


