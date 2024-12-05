def check(keys):
    def output(serverId):
        key = keys[serverId]
        return key.apikey
    length = len(keys)
    ListOutput = []
    for i in range(length):
        if not ListOutput:
            ListOutput = [output(i)]
        elif ListOutput:
            ListOutput.append(output(i))
        return ListOutput