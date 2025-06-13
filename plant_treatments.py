class TreatmentInfo:
    treatments = {
        'Apple___Apple_scab': "Use fungicides like captan or myclobutanil. Prune infected leaves.",
        'Apple___Black_rot': "Remove mummified fruit. Apply fungicides during bloom and early fruit development.",
        'Apple___Cedar_apple_rust': "Remove nearby cedar trees. Apply fungicides such as mancozeb.",
        'Apple___healthy': "No treatment needed.",
        'Blueberry___healthy': "No treatment needed.",
        'Cherry_(including_sour)___Powdery_mildew': "Use sulfur-based sprays or potassium bicarbonate. Ensure good air circulation.",
        'Cherry_(including_sour)___healthy': "No treatment needed.",
        'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': "Use resistant hybrids. Apply fungicides like azoxystrobin.",
        'Corn_(maize)___Common_rust_': "Plant resistant varieties. Apply fungicides if severe.",
        'Corn_(maize)___Northern_Leaf_Blight': "Use resistant hybrids. Apply fungicides if necessary.",
        'Corn_(maize)___healthy': "No treatment needed.",
        'Grape___Black_rot': "Remove infected fruit. Spray fungicides like mancozeb or myclobutanil.",
        'Grape___Esca_(Black_Measles)': "Prune infected vines. No chemical treatment is fully effective.",
        'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': "Use fungicides and manage canopy to reduce humidity.",
        'Grape___healthy': "No treatment needed.",
        'Orange___Haunglongbing_(Citrus_greening)': "Control psyllid population. Remove and destroy infected trees.",
        'Peach___Bacterial_spot': "Use copper-based bactericides. Plant resistant varieties.",
        'Peach___healthy': "No treatment needed.",
        'Pepper,_bell___Bacterial_spot': "Apply copper-based sprays. Use resistant seeds.",
        'Pepper,_bell___healthy': "No treatment needed.",
        'Potato___Early_blight': "Use fungicides like chlorothalonil. Rotate crops annually.",
        'Potato___Late_blight': "Destroy infected plants. Apply systemic fungicides.",
        'Potato___healthy': "No treatment needed.",
        'Raspberry___healthy': "No treatment needed.",
        'Soybean___healthy': "No treatment needed.",
        'Squash___Powdery_mildew': "Apply neem oil or sulfur-based fungicides.",
        'Strawberry___Leaf_scorch': "Remove affected leaves. Apply fungicides such as captan.",
        'Strawberry___healthy': "No treatment needed.",
        'Tomato___Bacterial_spot': "Use copper sprays. Avoid overhead watering.",
        'Tomato___Early_blight': "Apply chlorothalonil or mancozeb. Remove debris.",
        'Tomato___Late_blight': "Use fungicides like chlorothalonil. Destroy infected plants.",
        'Tomato___Leaf_Mold': "Increase air circulation. Use fungicides like chlorothalonil.",
        'Tomato___Septoria_leaf_spot': "Prune infected leaves. Apply fungicides regularly.",
        'Tomato___Spider_mites Two-spotted_spider_mite': "Use insecticidal soap or neem oil.",
        'Tomato___Target_Spot': "Apply fungicides like chlorothalonil. Remove infected foliage.",
        'Tomato___Tomato_Yellow_Leaf_Curl_Virus': "Control whiteflies. Remove infected plants.",
        'Tomato___Tomato_mosaic_virus': "Remove infected plants. Disinfect tools and avoid tobacco products.",
        'Tomato___healthy': "No treatment needed."
    }

    @classmethod
    def get_treatment(cls, disease):
        return cls.treatments.get(disease, "Treatment information not available.")

