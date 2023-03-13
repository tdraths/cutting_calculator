
# Importing Packages
import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

logo_col1, logo_col2, logo_col3 = st.columns([1,1,1])
with logo_col1:
    st.write("")
with logo_col2:
    st.image("WDOC_Logo_Black.jpg")
with logo_col3:
    st.write("")


# App Title
st.title('Cutting & Blending Calculator')

# Global Variables
spirit_count = 0

perc_alc_1 = 0
perc_alc_2 = 0
perc_alc_3 = 0
perc_alc_4 = 0
perc_alc_5 = 0

vol_alc_1 = 0
vol_alc_2 = 0
vol_alc_3 = 0
vol_alc_4 = 0
vol_alc_5 = 0

abv_alc_1 = 0.0
abv_alc_2 = 0.0
abv_alc_3 = 0.0
abv_alc_4 = 0.0
abv_alc_5 = 0.0

water_required = 0.0

df = pd.DataFrame(columns=['Volume', 'ABV'])
df2 = pd.DataFrame()


# Functions to Use
def get_blend(strong_alcohol_volume, strong_alcohol_abv, weak_alcohol_volume, weak_alcohol_abv):

    blend_volume = (strong_alcohol_volume + weak_alcohol_volume) - ((strong_alcohol_volume + weak_alcohol_volume)*.027)

    blend_abv = ((strong_alcohol_volume*strong_alcohol_abv) + (weak_alcohol_volume*weak_alcohol_abv)) / (strong_alcohol_volume + weak_alcohol_volume)

    return blend_volume, blend_abv

def get_water_requirement(starting_volume, starting_abv, target_abv):
    water_required = ((starting_volume*starting_abv) - (target_abv*starting_volume)) / target_abv
    return water_required


# Step One - Setting the first blend specifics
st.header('Step One')

# Get Number of Spirits in Blend
qty = st.form('get_spirit_qty')
qty.subheader('How many spirits are in the blend')
spirit_count = qty.slider(label='',min_value=1, max_value=5, step=1)

# Get Desired Total Blend Volume
qty.subheader('Total Volume of Samples in mL or L:')
total_volume = qty.number_input(label='', min_value=0, max_value=5000, step=100)

# Get Desired Final Blend ABV
qty.subheader('Desired Final Blended ABV %:')
target_abv = qty.number_input(label='', min_value=0.0, max_value=70.0, value=46.0, step=0.5)

# Step One Submit Button
qty.form_submit_button('COMPLETE STEP ONE HERE')



# Step Two
st.header('Step Two')

# Get Details of Each Spirit in Blend
details = st.form('get_spirit_details')
with details:
    # If the total number of spirits in the blend is 1
    if spirit_count == 1:
        with st.container():
            st.subheader('Spirit 1 Details')
            perc_alc_1 = 100.0

            #vol_alc_1 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_1')
                    
            abv_alc_1 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_1')

            vol_alc_1 = total_volume*(perc_alc_1/100)

    # If the total number of spirits in the blend is 2
    if spirit_count == 2:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(' Spirit 1 Details')
            perc_alc_1 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_1')
            
            #vol_alc_1 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_1')
        
            abv_alc_1 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_1')

            vol_alc_1 = total_volume*(perc_alc_1/100)

        with col2:
            st.subheader('Spirit 2 Details')
            perc_alc_2 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_2')
            
            #vol_alc_2 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_2')
        
            abv_alc_2 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_2')

            vol_alc_2 = total_volume*(perc_alc_2/100)

    # If the total number of spirits in the blend is 3
    if spirit_count == 3:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader(' Spirit 1 Details')
            perc_alc_1 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_1')
            
            #vol_alc_1 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_1')
        
            abv_alc_1 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_1')

            vol_alc_1 = total_volume*(perc_alc_1/100)

        with col2:
            st.subheader('Spirit 2 Details')
            perc_alc_2 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_2')

            #vol_alc_2 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_2')
        
            abv_alc_2 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_2')

            vol_alc_2 = total_volume*(perc_alc_2/100)


        with col3:
            st.subheader('Spirit 3 Details')
            perc_alc_3 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_3')

            #vol_alc_3 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_3')
        
            abv_alc_3 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_3')

            vol_alc_3 = total_volume*(perc_alc_3/100)

    # If the total number of spirits in the blend is 4
    if spirit_count == 4:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.subheader(' Spirit 1 Details')
            perc_alc_1 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_1')
            
            #vol_alc_1 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_1')
            
            abv_alc_1 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_1')

            vol_alc_1 = total_volume*(perc_alc_1/100)

        with col2:
            st.subheader('Spirit 2 Details')
            perc_alc_2 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_2')
            
            #vol_alc_2 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_2')
            
            abv_alc_2 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_2')

            vol_alc_2 = total_volume*(perc_alc_2/100)

        with col3:
            st.subheader('Spirit 3 Details')
            perc_alc_3 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_3')

            #vol_alc_3 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_3')
        
            abv_alc_3 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_3')

            vol_alc_3 = total_volume*(perc_alc_3/100)

        with col4:
            st.subheader('Spirit 4 Details')
            perc_alc_4 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_4')

            #vol_alc_4 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_4')
            
            abv_alc_4 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_4')

            vol_alc_4 = total_volume*(perc_alc_4/100)


    # If the total number of spirits in the blend is 5
    if spirit_count == 5:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.subheader(' Spirit 1 Details')
            perc_alc_1 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_1')
            
            #vol_alc_1 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_1')
            
            abv_alc_1 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_1')

            vol_alc_1 = total_volume*(perc_alc_1/100)

        with col2:
            st.subheader('Spirit 2 Details')
            perc_alc_2 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_2')
            
            #vol_alc_2 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_2')
            
            abv_alc_2 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_2')

            vol_alc_2 = total_volume*(perc_alc_2/100)

        with col3:
            st.subheader('Spirit 3 Details')
            perc_alc_3 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_3')

            #vol_alc_3 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_3')
        
            abv_alc_3 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_3')

            vol_alc_3 = total_volume*(perc_alc_3/100)

        with col4:
            st.subheader('Spirit 4 Details')
            perc_alc_4 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_4')

            #vol_alc_4 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_4')
            
            abv_alc_4 = st.number_input('Spirit ABV %:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_4')

            vol_alc_4 = total_volume*(perc_alc_4/100)

        with col5:
            st.subheader('Spirit 5 Details')
            perc_alc_5 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_5')

            #vol_alc_4 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value=1000, value=500, step=1, key='vol_5')

            abv_alc_5 = st.number_input('Spirit ABV%:', min_value=48.0, max_value=70.0, value=63.0, step=0.05, key='abv_5')

            vol_alc_5 = total_volume*(perc_alc_5/100)

submitted = details.form_submit_button('COMPLETE STEP TWO HERE')


if submitted:
    blended_df = pd.DataFrame(index=['Blend Details'])
    if spirit_count == 1:
        water_used = get_water_requirement(vol_alc_1, abv_alc_1, target_abv)

        volume_after_dilution = vol_alc_1 + water_used
        volume_lost_to_contraction = volume_after_dilution*(3.71*100)
        total_blended_volume = volume_after_dilution - volume_lost_to_contraction

        st.write('Water Required: ', round(water_used, 2))
    
    if spirit_count == 2:
        blend_1_vol, blend_1_abv = get_blend(vol_alc_1, abv_alc_1, vol_alc_2, abv_alc_2)

        water_used = get_water_requirement(blend_1_vol, blend_1_abv, target_abv)

        volume_after_dilution = blend_1_vol + water_used
        volume_lost_to_contraction = volume_after_dilution*(3.71/100)
        total_blended_volume = volume_after_dilution - volume_lost_to_contraction

        blended_df['Prelim Blend Volume'] = round(volume_after_dilution,2)
        blended_df['Volume Lost to Contraction'] = round(volume_lost_to_contraction, 2)
        blended_df['Final Blend Volume'] = round(total_blended_volume, 2)

        st.subheader('Your Blend Details')
        st.table(blended_df)

        st.subheader('Water Needed For Cutting')
        st.write(round(water_used, 2))

    if spirit_count == 3:
        blend_1_vol, blend_1_abv = get_blend(vol_alc_1, abv_alc_1, vol_alc_2, abv_alc_2)

        blend_2_vol, blend_2_abv = get_blend(vol_alc_3, abv_alc_3, blend_1_vol, blend_1_abv)

        water_used = get_water_requirement(blend_2_vol, blend_2_abv, target_abv)

        volume_after_dilution = blend_2_vol + water_used
        volume_lost_to_contraction = volume_after_dilution*(3.71/100)
        total_blended_volume = volume_after_dilution - volume_lost_to_contraction

        blended_df['Prelim Blend Volume'] = round(volume_after_dilution,2)
        blended_df['Volume Lost to Contraction'] = round(volume_lost_to_contraction, 2)
        blended_df['Final Blend Volume'] = round(total_blended_volume, 2)

        st.subheader('Your Blend Details')
        st.dataframe(blended_df)

        st.subheader('Water Needed For Cutting')
        st.write(round(water_used, 2))

    if spirit_count == 4:
        blend_1_vol, blend_1_abv = get_blend(vol_alc_1, abv_alc_1, vol_alc_2, abv_alc_2)

        blend_2_vol, blend_2_abv = get_blend(vol_alc_3, abv_alc_3, blend_1_vol, blend_1_abv)

        blend_3_vol, blend_3_abv = get_blend(vol_alc_4, abv_alc_4, blend_2_vol, blend_2_abv)

        water_used = get_water_requirement(blend_3_vol, blend_3_abv, target_abv)

        volume_after_dilution = blend_3_vol + water_used
        volume_lost_to_contraction = volume_after_dilution*(3.71/100)
        total_blended_volume = volume_after_dilution - volume_lost_to_contraction

        blended_df['Prelim Blend Volume'] = round(volume_after_dilution,2)
        blended_df['Volume Lost to Contraction'] = round(volume_lost_to_contraction, 2)
        blended_df['Final Blend Volume'] = round(total_blended_volume, 2)

        st.subheader('Your Blend Details')
        st.dataframe(blended_df)

        st.subheader('Water Needed For Cutting')
        st.write(round(water_used, 2))

    if spirit_count == 5:
        blend_1_vol, blend_1_abv = get_blend(vol_alc_1, abv_alc_1, vol_alc_2, abv_alc_2)

        blend_2_vol, blend_2_abv = get_blend(vol_alc_3, abv_alc_3, blend_1_vol, blend_1_abv)

        blend_3_vol, blend_3_abv = get_blend(vol_alc_4, abv_alc_4, blend_2_vol, blend_2_abv)

        blend_4_vol, blend_4_abv = get_blend(vol_alc_5, abv_alc_5, blend_3_vol, blend_3_abv)

        water_used = get_water_requirement(blend_4_vol, blend_4_abv, target_abv)

        volume_after_dilution = blend_4_vol + water_used
        volume_lost_to_contraction = volume_after_dilution*(3.71/100)
        total_blended_volume = volume_after_dilution - volume_lost_to_contraction

        blended_df['Prelim Blend Volume'] = round(volume_after_dilution,2)
        blended_df['Volume Lost to Contraction'] = round(volume_lost_to_contraction, 2)
        blended_df['Final Blend Volume'] = round(total_blended_volume, 2)

        st.subheader('Your Blend Details')
        st.dataframe(blended_df)

        st.subheader('Water Needed For Cutting')
        st.write(round(water_used, 2))
        




