import streamlit as st
import os

st.sidebar.image('https://clipartcraft.com/images/deloitte-logo-transparent-4.png', use_column_width=True)
st.header("Details on the process")
st.markdown("""<hr style="height:2px;border:none;color:#9ACD66;background-color:#9ACD66;" /> """, unsafe_allow_html=True)

file = "BaseReport.docx"

file2 = "EnhancedReport.docx"


col1, col2, col3 = st.columns([5,5,5])

with col1:
    with open(file,'rb') as file:
        btn = st.download_button(
            label = 'Download Base Report',
            data = file,
            file_name = 'BaseReport.docx'
        )
# /Users/wcoakley/LocalCode/deployment-gi3-cheat/Gi3-cheat/Welcome.py
# /Users/wcoakley/LocalCode/deployment-gi3-cheat/Gi3-cheat/assets/BaseReport.docx
with col3:
    with open(file2,'rb') as file2:
        btn2 = st.download_button(
            label = 'Download Enhanced Report',
            data = file2,
            file_name = 'EnhancedReport.docx'
        )

with st.expander("See AI breakdown preview"):

    st.subheader("Question 1")
    st.write("""
    1: What is the specific field of science or technology in which the R&D will be undertaken?
Incorporating additional research findings, the development and advancement of 3D modeling and rendering technologies in the field of construction and property industry not only aim at improving the quality and precision of visual representations but also significantly leverage sustainability and environmental considerations. Advanced 3D modeling plays a crucial role in material waste reduction by enabling precise planning and simulation, ensuring optimal use of resources and minimizing excess. This precision aids in drastically lowering the environmental footprint associated with construction projects. Furthermore, these technologies enhance the optimization of natural light within buildings. By accurately simulating light interactions, architects can design spaces that make better use of daylight, reducing reliance on artificial lighting, and thus, lowering energy consumption. Additionally, these innovations support the design of energy-efficient buildings by facilitating the exploration of renewable resources and carbon footprint reduction through improved ventilation and passive solar heating designs. The sustainable site selection and construction processes are further optimized by these technologies, minimizing the disruption to natural landscapes and promoting eco-friendly material choices. Integration with additive manufacturing, or 3D printing, presents another frontier, where precise component construction minimizes waste and enables the use of recycled materials, encapsulating a holistic approach to sustainability in the construction sector. Overall, the adoption of advanced 3D modeling and rendering technologies significantly contributes to the environmental sustainability of construction and architecture by promoting efficient resource use, waste reduction, and energy optimization.
Research Questions
•	What are the current limitations and advances in 3D modeling and rendering technologies specific to architectural visualization
•	How do the Unreal Gaming Engine and 3DS Max specifically handle detailed geometries and large-scale models for non-gaming applications, and what are their limitations in architectural visualization
•	What specific innovations in computational geometry can improve the handling of complex geometries within virtual environments for the construction and property industry
•	In what ways is parallel computing, particularly through GPUs and Nvidia's CUDA, being utilized to enhance rendering performance in architectural modeling and what are the latest advancements in this area
•	How can automation and mathematical models be further developed to improve efficiency and precision in 3D modeling for construction and architecture
•	What specific challenges do companies face when localizing 3D modeling and rendering technologies for the Chinese market, including regulatory, linguistic, and cultural adaptations
•	How do current 3D modeling and rendering tools integrate with and adhere to local architectural visibility guidelines and light exposure regulations in different regions, specifically in China
•	Identify and evaluate potential advancements in the use of gaming engines (like Unreal Engine) and software (like 3DS Max) for non-gaming applications in the construction and property development sectors
•	What are the existing and emerging companies focusing on the development and advancement of 3D modeling and rendering technologies for real estate and construction, and how do their solutions compare
•	Research the impact of enhanced GPU capabilities on the future of architectural engineering and whether there are emerging technologies or competitors to Nvidia's CUDA platform
•	How do current technologies address the issue of accurately representing earth curvature effects over large distances in virtual architectural models, and what innovations are on the horizon in this area
•	Investigate the potential for cross-disciplinary collaboration between computer graphics, parallel computing, and architectural engineering to address existing challenges in realistic, large-scale 3D environment rendering
•	What are the implications of advanced 3D modeling and rendering technologies on sustainability and environmental considerations in construction and architecture, including material waste reduction and optimization of natural light

Source Links:
•	https://uvu.edu/catalog/current/courses/eng-graphics-design-tech/
•	https://www.easyrender.com/a/3d-visualization-and-sonys-spatial-reality-display-is-it-applicable-in-architecture
•	https://www.techtarget.com/searchenterpriseai/definition/generative-AI
•	https://nap.nationalacademies.org/read/4761/chapter/12
•	https://www.sciencedirect.com/science/article/pii/S1474034620300914
Thought Process:
Sub-Question: What are the current limitations and advances in 3D modeling and rendering technologies specific to architectural visualization
        Intermediate Answer: A special problems course in architectural drafting. Teaches how to layout and detail a floor plan using a 3D modeling package. Software fee of $18 applies. Lab ... One of the most buzzing new technological advancements in architecture is Sony's brand new Spatial Reality Display. ... model or renders ... The current limitations ... Generative AI is a type of artificial intelligence technology that can produce various types of content. Find out how it works and why it's a hot commodity. Specifically, should ... modeling is a vital enabling technology whose limitations may impede progress. ... current assumptions concerning VE architectural ... Augmented Reality (AR) and Virtual Reality (VR) are technologies of utmost importance for the Architecture, Engineering and Construction (AEC) sectors as the ... ... specific frame rate) of a 3D model ... advanced architectural design, from RealSpace3d's ... 3D modeling and rendering software to visualize designs of modern ... Aug 15, 2022 ... Streamline collaboration: Technology advancements such as Building Information Modeling (BIM) help everybody involved in a project stay on the ... Indeed remote sensing technologies and methodologies for Cultural Heritage 3D documentation and modeling [10] allow the generation of very realistic 3D results ... Jan 7, 2024 ... ... architectural visualization without requiring extensive knowledge of 3D modeling and rendering software. These tools allow clients to ... Sep 13, 2018 ... Specifically, by default, 3D rendering ... 3D Visualization: Volume Rendering. The most ... Technology Advancements to Quickly Create 3D Models.

        """)


with st.expander('See code example'):
    st.code("""llm = OpenAI(temperature=0)
search = GoogleSerperAPIWrapper()
tools = [
        Tool(
            name="Intermediate Answer",
            func=search.results,
            description="useful for when you need to ask with search"
        )
]

self_ask_with_search_result = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True, return_intermediate_steps = True)""",language='python')
