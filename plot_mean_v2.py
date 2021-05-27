import glob
import numpy as np
from tensorflow.python.summary.summary_iterator import summary_iterator
import matplotlib.pyplot as plt
import argparse
import sys

def main(args):
    """ """
    paths = glob.glob(args.path + "/*")
    print(paths)
    print("different files ", len(paths))
    results = []
    name = args.key
    print("name ", name)
    for f in paths:
        tmp = []
        for e in summary_iterator(f):
            for v in e.summary.value:
                if args.debug:
                    print(v)
                if v.tag == name:
                    tmp.append(v.simple_value)
        length = args.length
        print("length tmp", len(tmp))
        tmp = tmp[:length]
        smooth = []
        for i in range(1, len(tmp)):
            if i -100 < 0:
                smooth.append(np.mean(tmp[:i]))
            else:
                smooth.append(np.mean(tmp[i-100:i]))
        results.append(smooth)

    results = np.array(results)
    print("result shape", results.shape)
    #print("result shape", results)
    mean = np.mean(results, axis=0)
    var = np.std(results, axis=0)
    print(results.shape)
    print("mean", mean.shape)
    #print("mean", mean)
    print("var", var.shape)
    #print("var", var)

    steps = [x for x in range(mean.shape[0])]
    plt.fill_between(steps, mean - var, mean + var, alpha=0.2, color='r')
    l1 =plt.plot(steps, mean,color='r', label=args.label1)
    title = args.title + "_metric_" + str(args.key)
    plt.title(title)
    #plt.legend(handles=[l1, l2], loc='upper left')
    plt.legend(loc='upper left')
    # plt.legend()
    y_min = np.min(mean) - (np.max(var) * 0.4) 
    y_max = np.max(mean) + (np.max(var) * 0.4) 
    plt.ylim(y_min, y_max)
    plt.xlabel(args.xlabel)
    plt.ylabel(args.ylabel)
    args.save_name = args.save_name + "_metric_" + str(args.key) + ".png"
    print("save image ", args.save_name)
    plt.savefig(args.save_name)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', type=str)
    parser.add_argument('--save_name', default="default.png", type=str)
    parser.add_argument('--path', default="", type=str)
    parser.add_argument('--title', default="", type=str)
    parser.add_argument('--label1', default= "eval_reward", type=str)
    parser.add_argument('--xlabel', default="20000 steps", type=str)
    parser.add_argument('--length', default=0, type=int)
    parser.add_argument('--ylabel', default="", type=str)
    parser.add_argument('--debug', default=False, type=bool)
    args = parser.parse_args()
    main(args)

