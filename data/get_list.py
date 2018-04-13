import sys
import os


def getlist(data_dir):
    train_dir = os.path.join(data_dir, 'train')
    test_dir = os.path.join(data_dir, 'test')
    train_file = open('train.txt', 'w')
    test_file = open('test.txt', 'w')
    for dir_name in cat_dir.keys():
        label = cat_dir[dir_name]
        tmp_train_dir = os.path.join(train_dir, dir_name)
        tmp_test_dir = os.path.join(test_dir, dir_name)
        files = os.listdir(tmp_train_dir)
        for f in files:
            train_file.write('{} {}\n'.format(os.path.join('train', dir_name, f), label))
        files = os.listdir(tmp_test_dir)
        for f in files:
            test_file.write('{} {}\n'.format(os.path.join('test', dir_name, f), label))
    train_file.close()
    test_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python get_list.py [cat_demo dir]')
        exit(1)
    data_dir = sys.argv[1]
    cat_dir = {'cat0': 0, 'cat1': 1}
    getlist(data_dir)
