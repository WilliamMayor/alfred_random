import alp


def main(args):
    try:
        args = args[0].split(' ')
    except:
        pass
    alp.log(args)
    try:
        try:
            _min = int(args[0])
            _max = int(args[1])
        except:
            _min = 0
            _max = int(args[0])
    except:
        _min = 0
        _max = 10
    items = []
    items.append(alp.Item(
        title='Generate Random Simple String',
        subtitle='%d letters long' % _max,
        arg='simple %d' % _max))
    items.append(alp.Item(
        title='Generate Random Strong String',
        subtitle='%d letters long' % _max,
        arg='strong %d' % _max))
    items.append(alp.Item(
        title='Generate Random Integer',
        subtitle='Between %d and %d' % (_min, _max),
        arg='integer %d %d' % (_min, _max)))
    items.append(alp.Item(
        title='Generate Random Float',
        subtitle='Between %d and %d' % (_min, _max),
        arg='float %d %d' % (_min, _max)))
    items.append(alp.Item(
        title='Generate Random Float',
        subtitle='Between 0 and 1',
        arg=''))
    alp.feedback(items)

if __name__ == '__main__':
    main(alp.args())