Dictionary Keys 
#We can set the key name of dictionary in number also.
#We can set the key name with Boolean value True or False also.
# A key needs to be immutable, keys cannot be changed. Lists can be changed. A dictionary key always has to be immutable. We cannot use a list as a key name.
# A key must be unique.

dict = {
  123: [1,2,3],
  True: 'Hi',
  'is_magic': False
  #[100]: True ---------it cannot be used as a key
}
print(dict[True])