import pickle
my_list = [1,2,3,4,5]
my_dict = {'name':'anvitha'}
my_str = 'asm tech'
f = open('test.txt','w')
#my_list = pickle.load(f)
#print my_list
pickle.dump(my_list,f)
pickle.dump(my_dict,f)
f.close
        
