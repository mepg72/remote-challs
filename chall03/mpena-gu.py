#!/usr/bin/env python3
import sys

def get_argv_list(argv):
    argv_row = []
    while argv:
        argv_row.append(argv[:1])
        argv = argv[1:]
    return argv_row

def create_squared_rows(list_argv):
    alist = []
    matrix_list = []
    for argv in list_argv:
        alist = get_argv_list(argv)
        matrix_list.append(alist)
    return matrix_list

def check_argv():
    if len(sys.argv) < 2 or len(sys.argv) > 21:
        return False
    else:
        list_row = sys.argv[1:] 
        len_ref_argv = len(list_row[0])
        num_row = len(list_row)
        if num_row == 1 and len_ref_argv > 1:
            return False
        elif num_row == 2 and len_ref_argv > 2:
            return False
        elif num_row > 2 and num_row != len_ref_argv:
            return False
        else:
            num_argv = 0 
            for argv in list_row:
                num_argv += 1 
                len_argv = len(argv)
                if not argv.isdigit() or len_argv != len_ref_argv:
                    return False
        return True

def snail (row_init, row_end, col_init, col_end, squared_rows):
    snail_result =[]
    if row_init == row_end and col_init == col_end:
        snail_result.append(squared_rows[row_init][col_init])
    for row in range (row_init, row_end, 1):
        if row == row_init:
            for col in range(col_init, col_end):
                snail_result.append(squared_rows[row][col])
        elif row == (row_end - 1):
            for col in reversed(range(col_init, col_end)):
                snail_result.append(squared_rows[row][col])
        else:
             snail_result.append(squared_rows[row][col_end-1])
    for row in reversed(range (row_init + 1, row_end - 1)):
        snail_result.append(squared_rows[row][col_init])
    snail_str = ", ".join(snail_result)
    return snail_str

def resolve():
    if len(sys.argv[1:]) == 1:
        print("%s" % sys.argv[1])
    elif len(sys.argv[1:]) == 2 and len(sys.argv[1]) == 1:
        print("%s, %s" % (sys.argv[1],sys.argv[2]))
    else:
        size_array = len(sys.argv[1])
        squared = create_squared_rows(sys.argv[1:])
        num_squared = size_array//2 
        if size_array%2 != 0:
            num_squared += 1
        i = 0 
        snail_result = "" 
        while i< num_squared:
            if i>0:
                snail_result += ', '
            row_init = i
            row_end  = size_array - i
            col_init = i
            col_end  = size_array - i
            snail_result += snail(row_init,row_end,col_init,col_end, squared)
            i += 1
        print(snail_result)

def main():
    if not check_argv():
        sys.exit("usage: %s <1-9 squared_rows...>" % sys.argv[0])
    resolve()

if __name__ == "__main__":
    main()
