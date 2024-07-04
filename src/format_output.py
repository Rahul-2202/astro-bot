charts_info = {
    "Rasi": {
        "description": "The Rasi chart, also known as the natal chart or birth chart, is the primary chart in Vedic astrology. It represents the positions of the planets at the time of an individual's birth. This chart provides a comprehensive overview of a person's personality, life path, strengths, and weaknesses. It is fundamental for overall analysis and interpretation of an individual's horoscope."
    },
    "Navamsa": {
        "description": "The Navamsa chart, also known as the D9 chart, is a divisional chart derived from the main Rasi chart. It is used for assessing marriage, relationships, and spiritual inclinations. This chart is crucial for understanding the finer aspects of an individual's life, particularly marital and spiritual matters."
    },
    "Hora": {
        "description": "The Hora chart, or the D2 chart, divides each sign into two parts. It is used for analyzing wealth, financial prospects, and resources. This chart is important for understanding an individual's financial status and wealth accumulation potential."
    },
    "Drekkana": {
        "description": "The Drekkana chart, or the D3 chart, divides each sign into three parts. It focuses on siblings, courage, and efforts. This chart helps in understanding relationships with siblings and the nature of an individual's efforts and initiatives."
    },
    "Chaturthamsa": {
        "description": "The Chaturthamsa chart, or the D4 chart, is used for analyzing properties, fixed assets, and overall happiness. This chart is crucial for understanding matters related to property and home life."
    },
    "Panchamsa": {
        "description": "The Panchamsa chart, or the D5 chart, is associated with intelligence, knowledge, and children. This chart is important for assessing creativity, intellectual abilities, and progeny."
    },
    "Shasthamsa": {
        "description": "The Shasthamsa chart, or the D6 chart, focuses on health, diseases, and obstacles. This chart is essential for analyzing health issues and potential challenges in life."
    },
    "Saptamsa": {
        "description": "The Saptamsa chart, or the D7 chart, is used for analyzing progeny and reproductive potential. This chart is important for understanding matters related to children and lineage."
    },
    "Ashtamsa": {
        "description": "The Ashtamsa chart, or the D8 chart, is related to longevity, sudden events, and inheritance. This chart is crucial for understanding life span, unexpected changes, and inherited wealth."
    },
    "Dasamsa": {
        "description": "The Dasamsa chart, or the D10 chart, focuses on career, profession, and public life. This chart is essential for analyzing professional success and career prospects."
    },
    "Rudramsa": {
        "description": "The Rudramsa chart, or the D11 chart, is associated with gains, achievements, and friends. This chart is important for understanding financial gains and social network."
    },
    "Dwadasamsa": {
        "description": "The Dwadasamsa chart, or the D12 chart, is used for analyzing parental influences and family heritage. This chart is crucial for understanding one's relationship with parents and ancestral lineage."
    },
    "Shodasamsa": {
        "description": "The Shodasamsa chart, or the D16 chart, focuses on vehicles, luxuries, and comforts. This chart is important for assessing one's enjoyment of material comforts and luxuries."
    },
    "Vimsamsa": {
        "description": "The Vimsamsa chart, or the D20 chart, is associated with spiritual progress and religious inclinations. This chart is crucial for understanding an individual's spiritual journey and religious activities."
    },
    "Siddhamsa": {
        "description": "The Siddhamsa chart, or the D24 chart, focuses on education, learning, and scholarly pursuits. This chart is important for assessing academic success and intellectual capabilities."
    },
    "Nakshatramsa": {
        "description": "The Nakshatramsa chart, or the D27 chart, is associated with detailed analysis of mental stability and temperament. This chart is crucial for understanding psychological traits and emotional well-being."
    },
    "Trimsamsa": {
        "description": "The Trimsamsa chart, or the D30 chart, focuses on misfortunes, diseases, and hidden weaknesses. This chart is important for identifying potential challenges and vulnerabilities."
    },
    "Khavedamsa": {
        "description": "The Khavedamsa chart, or the D40 chart, is associated with auspicious and inauspicious effects in life. This chart is crucial for a detailed understanding of specific influences on one's life."
    },
    "Shashtyamsa": {
        "description": "The Shashtyamsa chart, or the D60 chart, focuses on past life karma and its effects on the current life. This chart is important for a comprehensive understanding of karmic influences and life purpose."
    }
}


def structure_chart_output(chart_name, output):
    # Initialize the structured output dictionary
    structured_output = {
        "chart_name": chart_name,
        "charts_description": charts_info[chart_name]["description"],
        "data": []
    }
    
    # Iterate through the output dictionary to structure each celestial body
    for key, data in output.items():
      if "name" in data and "current_sign" in data and "isRetro" in data:
        structured_output["data"].append({
          "name": data["name"],
          "current_sign": data["current_sign"],
          "is_retrograde": data["isRetro"].lower() == "true"
        })
        if chart_name == "Rasi" and "fullDegree" in data and "normDegree" in data:
          structured_output["data"][-1]["full_degree"] = data["fullDegree"]
          structured_output["data"][-1]["normalized_degree"] = data["normDegree"]
    
    return structured_output


# def format_rasi_chart(output):
#     formatted_output = []
#     celestial_bodies = [
#         "Ascendant", "Sun", "Moon", "Mars", "Mercury", "Jupiter",
#         "Venus", "Saturn", "Rahu", "Ketu", "Uranus", "Neptune", "Pluto"
#     ]

#     formatted_output.append("Rasi Chart Output:\n")
#     for body in celestial_bodies:
#         if body in output[1]:
#             body_data = output[1][body]
#             formatted_output.append(f"{body}:\n")
#             formatted_output.append(f"  Current Sign: {body_data['current_sign']}\n")
#             formatted_output.append(f"  Full Degree: {body_data['fullDegree']:.2f}\n")
#             formatted_output.append(f"  Normalized Degree: {body_data['normDegree']:.2f}\n")
#             formatted_output.append(f"  Retrograde: {body_data['isRetro'].capitalize()}\n")

#     return ''.join(formatted_output)

# # Example usage
output = [
    {
        "0": {"name": "Ascendant", "fullDegree": 260.15231949660466, "normDegree": 20.15231949660466, "isRetro": "false", "current_sign": 9},
        "1": {"name": "Sun", "fullDegree": 114.60861229742005, "normDegree": 24.608612297420052, "isRetro": "false", "current_sign": 4},
        "2": {"name": "Moon", "fullDegree": 285.033591796012, "normDegree": 15.03359179601199, "isRetro": "false", "current_sign": 10},
        "3": {"name": "Mars", "fullDegree": 30.51014898802912, "normDegree": 0.510148988029119, "isRetro": "false", "current_sign": 2},
        "4": {"name": "Mercury", "fullDegree": 137.2368977501939, "normDegree": 17.23689775019389, "isRetro": "false", "current_sign": 5},
        "5": {"name": "Jupiter", "fullDegree": 344.25277484744237, "normDegree": 14.252774847442367, "isRetro": "true", "current_sign": 12},
        "6": {"name": "Venus", "fullDegree": 95.45879340497692, "normDegree": 5.458793404976916, "isRetro": "false", "current_sign": 4},
        "7": {"name": "Saturn", "fullDegree": 297.966845952626, "normDegree": 27.966845952625988, "isRetro": "true", "current_sign": 10},
        "8": {"name": "Rahu", "fullDegree": 23.585811806879523, "normDegree": 23.585811806879523, "isRetro": "true", "current_sign": 1},
        "9": {"name": "Ketu", "fullDegree": 203.58581180687952, "normDegree": 23.58581180687952, "isRetro": "true", "current_sign": 7},
        "10": {"name": "Uranus", "fullDegree": 24.70916691303532, "normDegree": 24.70916691303532, "isRetro": "false", "current_sign": 1},
        "11": {"name": "Neptune", "fullDegree": 330.7897522887296, "normDegree": 0.7897522887295736, "isRetro": "true", "current_sign": 12},
        "12": {"name": "Pluto", "fullDegree": 272.6477453110886, "normDegree": 2.647745311088613, "isRetro": "true", "current_sign": 10},
        "13": {"name": "ayanamsa", "value": 24.168807418791342},
        "debug": {"observation_point": "topocentric", "ayanamsha": "lahiri"}
    },
    {
        "Ascendant": {"current_sign": 9, "fullDegree": 260.15231949660466, "normDegree": 20.15231949660466, "isRetro": "false"},
        "Sun": {"current_sign": 4, "fullDegree": 114.60861229742005, "normDegree": 24.608612297420052, "isRetro": "false"},
        "Moon": {"current_sign": 10, "fullDegree": 285.033591796012, "normDegree": 15.03359179601199, "isRetro": "false"},
        "Mars": {"current_sign": 2, "fullDegree": 30.51014898802912, "normDegree": 0.510148988029119, "isRetro": "false"},
        "Mercury": {"current_sign": 5, "fullDegree": 137.2368977501939, "normDegree": 17.23689775019389, "isRetro": "false"},
        "Jupiter": {"current_sign": 12, "fullDegree": 344.25277484744237, "normDegree": 14.252774847442367, "isRetro": "true"},
        "Venus": {"current_sign": 4, "fullDegree": 95.45879340497692, "normDegree": 5.458793404976916, "isRetro": "false"},
        "Saturn": {"current_sign": 10, "fullDegree": 297.966845952626, "normDegree": 27.966845952625988, "isRetro": "true"},
        "Rahu": {"current_sign": 1, "fullDegree": 23.585811806879523, "normDegree": 23.585811806879523, "isRetro": "true"},
        "Ketu": {"current_sign": 7, "fullDegree": 203.58581180687952, "normDegree": 23.58581180687952, "isRetro": "true"},
        "Uranus": {"current_sign": 1, "fullDegree": 24.70916691303532, "normDegree": 24.70916691303532, "isRetro": "false"},
        "Neptune": {"current_sign": 12, "fullDegree": 330.7897522887296, "normDegree": 0.7897522887295736, "isRetro": "true"},
        "Pluto": {"current_sign": 10, "fullDegree": 272.6477453110886, "normDegree": 2.647745311088613, "isRetro": "true"}
    }
]

# print(format_rasi_chart(output))


# def format_chart_output(chart_name, output):
#     # Initialize the formatted output string with the chart name
#     formatted_output = f"{chart_name} Chart Output:\n"
    
#     # Iterate through the output dictionary to format each celestial body
#     for key, data in output.items():
#         formatted_output += f"{data['name']}:\n"
#         formatted_output += f"  Current Sign: {data['current_sign']}\n"
#         formatted_output += f"  Retrograde: {data['isRetro'].capitalize()}\n\n"
    
#     return formatted_output

# # Example usage
# navamsa_output = {
#     "statusCode": 200,
#     "output": {
#         "0": {"name": "Ascendant", "isRetro": "false", "current_sign": 7},
#         "1": {"name": "Sun", "isRetro": "false", "current_sign": 7},
#         "2": {"name": "Moon", "isRetro": "false", "current_sign": 5},
#         "3": {"name": "Mars", "isRetro": "false", "current_sign": 9},
#         "4": {"name": "Mercury", "isRetro": "false", "current_sign": 10},
#         "5": {"name": "Jupiter", "isRetro": "false", "current_sign": 11},
#         "6": {"name": "Venus", "isRetro": "false", "current_sign": 6},
#         "7": {"name": "Saturn", "isRetro": "false", "current_sign": 9},
#         "8": {"name": "Rahu", "isRetro": "true", "current_sign": 4},
#         "9": {"name": "Ketu", "isRetro": "true", "current_sign": 10},
#         "10": {"name": "Uranus", "isRetro": "false", "current_sign": 7},
#         "11": {"name": "Neptune", "isRetro": "false", "current_sign": 4},
#         "12": {"name": "Pluto", "isRetro": "false", "current_sign": 11}
#     }
# }

# print(format_chart_output("Navamsa", navamsa_output['output']))


navamsa_output = {
    "statusCode": 200,
    "output": {
        "0": {"name": "Ascendant", "isRetro": "false", "current_sign": 7},
        "1": {"name": "Sun", "isRetro": "false", "current_sign": 7},
        "2": {"name": "Moon", "isRetro": "false", "current_sign": 5},
        "3": {"name": "Mars", "isRetro": "false", "current_sign": 9},
        "4": {"name": "Mercury", "isRetro": "false", "current_sign": 10},
        "5": {"name": "Jupiter", "isRetro": "false", "current_sign": 11},
        "6": {"name": "Venus", "isRetro": "false", "current_sign": 6},
        "7": {"name": "Saturn", "isRetro": "false", "current_sign": 9},
        "8": {"name": "Rahu", "isRetro": "true", "current_sign": 4},
        "9": {"name": "Ketu", "isRetro": "true", "current_sign": 10},
        "10": {"name": "Uranus", "isRetro": "false", "current_sign": 7},
        "11": {"name": "Neptune", "isRetro": "false", "current_sign": 4},
        "12": {"name": "Pluto", "isRetro": "false", "current_sign": 11}
    }
}

print(structure_chart_output("Navamsa", navamsa_output['output']))
print("rasi")
print(structure_chart_output("Rasi", output[0]))
