def convert_labels(path, x1, y1, x2, y2):
    """
    Definition: Parses label files to extract label and bounding box
        coordinates.  Converts (x1, y1, x1, y2) KITTI format to
        (x, y, width, height) normalized YOLO format.
    """
    def sorting(l1, l2):
        if l1 > l2:
            lmax, lmin = l1, l2
            return lmax, lmin
        else:
            lmax, lmin = l2, l1
            return lmax, lmin
    size = get_img_shape(path)
    xmax, xmin = sorting(x1, x2)
    ymax, ymin = sorting(y1, y2)
    dw = 1./size[1]
    dh = 1./size[0]
    x = (xmin + xmax)/2.0
    y = (ymin + ymax)/2.0
    w = xmax - xmin
    h = ymax - ymin
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)def get_img_shape(path):
    path = 'data/'+path
    img = cv2.imread(path)
    try:
        return img.shape
    except AttributeError:
        print('error! ', path)
        return (None, None, None)bbox_img['x'], bbox_img['y'], bbox_img['width'], bbox_img['height'] = zip(*bbox_img.progress_apply(lambda row: convert_labels(row['Path'], row['x1'], row['y1'], row['x2'], row['y2']), axis=1)) # Like python for one lone code.df = bbox_img.merge(train_test_valid_anot).merge(categories_img)
df.to_csv('data/Anno/annotation_w-o_atr.csv', index=False)y