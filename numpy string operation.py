 x=np.char.encode("salem",encoding='cp500')

x
Out[11]: array(b'\xa2\x81\x93\x85\x94', dtype='|S5')

np.char.decode(x,encoding='cp500')
Out[12]: array('salem', dtype='<U5')



np.char.splitlines("salem salem salem salem",keepends=3)
Out[28]: array(list(['salem salem salem salem']), dtype=object)

np.char.zfill("salem",width=15)
Out[29]: array('0000000000salem', dtype='<U15')


np.char.rjust("salem",20,fillchar='$')
Out[15]: array('$$$$$$$$$$$$$$$salem', dtype='<U20')

np.char.swapcase("sAlEm")
Out[16]: array('SaLeM', dtype='<U5')

np.char.lower("SALEM")
Out[17]: array('salem', dtype='<U5')

np.char.title("SALEM")
Out[18]: array('Salem', dtype='<U5')

np.char.isalpha("salem")
Out[19]: array(True)

np.char.isnumeric("salem")
Out[20]: array(False)

np.char.isdigit("salem")
Out[21]: array(False)

np.char.isupper("salem")
Out[22]: array(False)


 np.char.join('-',"salem")
Out[24]: array('s-a-l-e-m', dtype='<U9')

np.char.partition("salem",',')
Out[25]: array(['salem', '', ''], dtype='<U5')

np.char.rstrip("salem",chars='%')
Out[26]: array('salem', dtype='<U5')