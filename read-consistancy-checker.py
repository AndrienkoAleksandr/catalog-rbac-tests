# The idea of this script is to check the consistancy of the read data, since we created new role.
# Also we check delay of the response. 
# This scripts allows to make a lot of parallel read requests to make small dos attack to the API and make
#  sure backend can handle a lot of requests without failing.
# In the newer rbac-backend we will try have in sync data beetwen few pod replicase, 
# we need to make sure that read operations are consistent and stable even with large amount of requests.

