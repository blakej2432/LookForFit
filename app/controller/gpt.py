from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.2)

equipment = "랫풀다운"

example = '''
        **운동부위**
        
        - 가슴

        **운동방법**

        1. 등판과 엉덩이판의 위치를 C에 맞춰주세요.

        2. 시작자세는 손잡이가 가슴 중앙에 오도록 합니다.

        3. 가슴을 내밀고 허리를 아치로 고정하여 팔꿈치를 앞으로 밀면서 가슴을 수축하며 동작합니다.


        **주의사항**

        팔꿈치와 손목의 위치를 평행이 되도록 주의해주세요.

        **운동효과**

        이 운동은 특히 가슴 근육의 크기와 강도를 증가시키며, 가슴의 아랫부분을 중심으로 한 근육을 주로 발달시킵니다. 또한, 이 운동은 근력과 근지구력을 향상시키며, 상체 균형을 유지하는 데도 도움이 됩니다.

'''

template = '''
        You're a personal fitness trainer trainer. You know a lot about anatomy and the human body, as well as how to use gym equipment, exercise techniques, and safety precautions at the gym.
        You'll be answering questions from trainee with memberships based on the principles of muscle function and effective strength training methods. 
        please answer questions in korean.

        Follow the format when answering a question. but the format of the answer should be markdown:
        {example}

        the format of the output must be markdown.

        Incorporate anatomical and exercise physiological knowledge to include precautions and exercise effects as well.
        Instead of rambling on, answer in a concise and digestible manner. Use simple terms to make it easy for beginners to understand.
        Tell me how to work out with this equipment:
        {equipment}
        '''

prompt_template = PromptTemplate(
    template=template,
    input_variables=["example", "equipment"],
)

chain = prompt_template | llm | StrOutputParser()
chain.invoke({"example":example, "equipment":equipment})