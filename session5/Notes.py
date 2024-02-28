rule all:
    input:
        # expand creates a list with a variable path name, session_id takes on values 1, then 2 etc
        expand("figures/subjet_one/response_time{session_id}_hist.png", session_id[1,2])

rule make_histogram:
    input: "data/raw/subject_one/response_time{session_id}.npy"
    output: "figures/subject_one/response_time{session_id}_hist.npy"
    run: 
        # here your code goes
        # input and output are just strings