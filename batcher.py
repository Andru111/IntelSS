import scipy as sp

class batcher:

    def __init__(self, data):
        self.data = data
        print('batcher initialize')

    def tth_create(self):
        new_data = {}
        temp_list = {}
        teacher_list = self.data[:, 1]
        cur_teacher = teacher_list[0]
        temp_list[0] = cur_teacher
        prev_idx = 0
        next_idx = 0
        idx = 0
        for i in range(teacher_list.__len__()):
            if teacher_list[i] != cur_teacher:
                cur_teacher = teacher_list[i]
                next_idx = i
                new_data[idx] = self.data[prev_idx : next_idx][:]
                temp_list[idx+1] = cur_teacher
                idx += 1
                prev_idx = i

        new_data[idx] = self.data[prev_idx : teacher_list.__len__()][:]
        self.tth = new_data
        self.name_list = temp_list
        return new_data
