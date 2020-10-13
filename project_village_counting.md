# Small project discussion:

## About Project:

Hum ek project bana rahe hain. Jisme hum pahle ek village ke sabhi family ki details ko store karne. Then is tarike se hi hum bad me multiplal villages ka data store karenge.

Yaha par har ek village ke name se folder create karna then use village folder me family wise files bana kar store karna.

Ye sara kaam process wise hona hai. So iski details niche point wise batai gai hain.

## Village Project Details:

1. hame village wise data store karna hai.
1. ek village me aane wale sabhi logo ka registration karna hai.
1. aur har ek familiy ki detail individual file me store karna hai.
1. Registration formate kuch aysa hoga:

        -------------------------------------------
                    ABC's Family Detail
        -------------------------------------------
        Village:
        -------------------------------------------
        Main Person 1:
        Person 2:   ()
        Person 3:   ()
        Person 4:   ()
        Person 5:   ()
        Person 6:   ()
        Person 7:   ()
        Person 8:   ()
        Person 9:   ()
        Person 10:   ()
        -------------------------------------------
        Total Family Members:
        -------------------------------------------
## Step 1:

1. Create main.py file jaha par hum user se input le rahe hain:
        1. show villages list:
                1. Chekc village_list.txt file first for available village.
                        1. agar file me villages availabel hai to show karenge
                        2. Otherwise new village create karna ka option denge
                2. Agar village exist karta hain then: 
                        1. hum user ko new family register karne ka option denge
                        2. Hum existing family dekhne ka option denge.
        2. create new village:
                1. Village folder create karte time is village ki detail ek villagelist.txt file me bhi store karna hai.
                2. Agar village exist karta hain then: 
                        1. hum user ko new family register karne ka option denge.

1. Total village me kitni familys hain uska count check karna.

Note: Jo bhi village ka name hai usko har faimily data me add karna hai.