import streamlit as st 

from utills.database import(
    insert_health_data
)


st.set_page_config(
    page_title="Threshold version 0.0.1",
    page_icon="💻",
    layout="wide"
)

# ----------------- SESSION STATE INTITIALIZATION-----------------
if "step_count" not in st.session_state:
    st.session_state.step_count = 0
if "sleep_hours" not in st.session_state:
    st.session_state.sleep_hours = 0
if "water_intake" not in st.session_state:
    st.session_state.water_intake = "not completed"
if "submitted" not in st.session_state:
    st.session_state.submitted = False
    
#------------------------------------------------------------------    
     

st.header("Welcome to threshold community",)


#-------------------SUBHEADER---------------------

with st.sidebar:
    st.title("💻Threshold")
    
    st.divider()
    
    page = st.radio("Navigation", ["Dashboard"])
    
    st.divider()
    
    st.subheader("Appp info")
    st.write("Version 0.0.1")
        

st.divider()

left, right = st.columns([1,2], vertical_alignment="center", gap="large")

with left:
    st.subheader("Enter your data")
    with st.form("Data input section"):
        step_count = st.number_input("Enter your stepcounts")
        sleep_hours = st.number_input("enter your numbers of hours of sleep ", min_value=0, max_value=24, step=1)
        water_intake = st.selectbox("did you completed your 3l water goal today?", ["Completed", "Not completed"])
        
        
        submit = st.form_submit_button("submit")
        # SAVING DATA 
        if submit:
            st.session_state.step_count = step_count
            st.session_state.sleep_hours = sleep_hours
            st.session_state.water_intake = water_intake
            st.session_state.submitted = True
            
            # Database insert
            insert_health_data(
                step_count,
                sleep_hours,
                water_intake
            )
            
            st.success("Data saved successfully")

with right:
        if st.session_state.submitted:
            calories_burnt = (st.session_state.step_count*0.04) 
            
            #TABS 
            tab1,tab2,tab3 = st.tabs([
                "📊 Summary",
                "📈 Analytics",
                "🧠 Recommendations"
                
            ])
            
            with tab1: 
                
                with st.container():  
                    
                    st.subheader("Summary")
                    col3,col4,col5,col6 = st.columns(4)
                    
                    with col3:
                        st.metric("Stepcounts", st.session_state.step_count)
                    with col4:
                        st.metric("Calorie burnt", f"{calories_burnt:.2f}")
                    with col5:
                        st.metric("Sleep hours", st.session_state.sleep_hours)
                    with col6:
                        st.metric("Water intake goal status", st.session_state.water_intake ) 
                        
                st.divider()
                
                health_score = 0
                
                if st.session_state.step_count >= 7000:
                    health_score +=40
                    
                if st.session_state.sleep_hours >= 7:
                    health_score += 30
                    
                if st.session_state.water_intake == "Completed":
                    health_score +=30
                
                with st.container():
                    
                    st.subheader("Health score")
                    st.progress(health_score)
                    
                    st.metric("Overall Health Score", f"{health_score}/100")
                    if health_score < 40:
                        st.error("You can do better!")
                    elif 40<= health_score <= 70:
                        st.warning("You are showing progrsss") 
                    elif health_score > 70:
                        st.success("You are doing good")                              
            
            with tab2:
                
               with st.container():
                   
                    st.subheader("📈 Analytics")  
                    
                    st.line_chart([
                        st.session_state.step_count,
                        calories_burnt,
                        st.session_state.sleep_hours
                        ]) 
                    
                    
            with tab3:
                
                with st.container():
                    
                    st.subheader("🧠 Health Recommendations")    
                    
                    if 3 <st.session_state.sleep_hours<6:
                        st.warning("⚠️ Improve your sleep schedule")     
                    else:
                        st.success("✅ Sleep schedule looks healthy")  
                    if st.session_state.water_intake=="Not completed":
                        st.warning("❌ Complete your water goal") 
                    else:
                        st.success("💧 Water goal completed")  
                   
                            
                          
                        
        
        # st.divider()         
        
        # st.bar_chart([
        #         step_count,
                
        #     ] )
                 
                
# py -3.10 -m streamlit run main.py                