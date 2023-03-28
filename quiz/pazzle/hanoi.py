
def hanoi(disk: int, src: str, dest: str, via: str):
    '''
    Input:
    disk: the number of disk
    src: 移動元
    dest: 移動先
    via: 経由
    '''
    if disk < 1:
        return
    
    hanoi(disk-1, src, via, dest)
    print(f"move {disk} from {src} to {dest}")
    hanoi(disk-1, via, dest, src)



if __name__ == "__main__":
    hanoi(3, "A", "C", "B")