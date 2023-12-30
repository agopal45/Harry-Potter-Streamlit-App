import streamlit as st
import requests

#accessing harry potter api
r=requests.get("https://hp-api.onrender.com/api/characters")
data = r.json()

#Header
def intro():
    st.title("Welcome to Hogwarts! 🏰")
    st.image("images/hogwarts.jpeg", width = 500)
    st.subheader("✨Fill out these questions to select your wand, get sorted into a house, and discover your patronus:")
intro()



#Form
def form():
    name = st.text_input("What is your name?")
    tab1, tab2 = st.tabs(["🪄Wand & Patronus", "🧙House Sorting"])
    with tab1:
        st.subheader("🪄 Let's get started with your wand!")
        wand_length = st.slider("Use the slider to select your preferred wand length (Longer wands will have more power but less control and vice versa):", 8.0,
                                14.0,
                                9.5,
                                .25) #NEW
        woodtypes = ['holly', 'vine', 'hawthorn','fir', 'willow', 'cherry', 'yew', 'walnut', 'cedar', 'elm', 'cypress', 'oak', 'ash', 'hornbeam', 'alder', 'larch', 'chestnut']
        wand_wood = st.selectbox("Choose your desired wand wood:", woodtypes) #NEW
        wand_core = st.radio("Pick a wand core:", ("Unicorn Tail Hair","Phoenix Tail Feather", "Dragon Heartstring")) #NEW
        patronus = ""
        for charDict in data:
            if wand_wood == charDict["wand"]["wood"]:
                patronus = charDict["patronus"]
                image = charDict['image']
                comparison = charDict['name']
                if patronus != "":
                    break
                else:
                    patronus = "Non-Corporeal"
        if st.button('Submit'): #NEW
            st.write("‍Congratulations, {}. Your patronus is a {}!".format(name,patronus))
            st.write("This is the same patronus as", comparison + ".")
            if image != "":
                st.image(image)
    
    with tab2:
        st.image("images/sorthat.jpeg")
        st.subheader("🧙 \"Now it is time to get sorted into a house!\" ")
        house_choice = st.radio("Which of these activities appeals to you most?", ["a) Baking banana bread 🍌🍞",
                                                                    "b) Pranking civilians at Walmart 🃏",
                                                                    "c) Bouldering at a rock-climbing gym 🧗‍♀️",
                                                                    "d) Watching time-lapsed videos of sorting algorithms📱"])
        house_letter = house_choice[0]
        if st.button('See your house!'): 
            if house_letter == "a":
                house = "hufflepuff"
                houseEmoji = "🦡"
            elif house_letter == 'b':
                house = "slytherin"
                houseEmoji = "🐍"
            elif house_letter == "c":
                house = "gryffindor"
                houseEmoji = "🦁"
            elif house_letter == 'd':
                house = "ravenclaw"
                houseEmoji = "🐦"
            houseCrest = house + ".webp"
            st.image("images/"+houseCrest)
            st.header("Amazing job, " + name+ "! You are now the latest addition to house " + house.upper() +"! " + houseEmoji)
            link = "https://www.wizardingworld.com/fact-file/magical-miscellany/" + house
            st.link_button("Learn more about your house here!" , link) #NEW

form()

