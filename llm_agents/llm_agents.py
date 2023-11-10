from dotenv import load_dotenv
import json

# Required to load hidden variables from the environment
# In this case it is the API key for OpenAI
load_dotenv()

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

class CohortQualifier:
    """
    The `CohortQualifier` class is a Python class that uses a language model to classify companies into
    cohorts based on their descriptions.
    """
    
    def __init__(self):
   
        # Defined the standard prompt which tells the llm what to do
        self.prompt_scaffold = """
            You are a financial analyst. You need to assign a cohort according to the provided description of the company. From the list below choose which cohort best suits the company's description and return the result as a json file without any explanations or additional writing.

            cohorts list = [
                "AdTech",
                "Advertising Services",
                "Agencies / System Integrators",
                "Digital Marketing Agencies",
                "IT Services",
                "Management Consulting",
                "AI",
                "Conversational AI", 
                "Machine Vision",
                "Retail AI",
                "Business Intelligence",
                "AR / VR",
                "Automotive",
                "Customer Acquisition and Relationship Management (Automotive)",
                "Dealer Management Systems (Automotive)",
                "Dealership Management (Automotive)",
                "F&I (Automotive)",
                "F&I Technology (Automotive)",
                "Fixed Operations (Automotive)",
                "Inventory Management (Automotive)",
                "Inventory, Auctions & Reconditioning (Automotive)",
                "Listing Platforms (Automotive)",
                "Managed Marketplaces (Automotive)",
                "P2P Marketplaces (Automotive)",
                "Peer-to-Peer & Subscription (Automotive)",
                "Registration and Titling (Automotive)",
                "Rental & Subscription (Automotive)",
                "Business Process Outsourcing",
                "CPG",
                "Credit Union",
                "Crypto / Blockchain",
                "DNVB",
                "Health & Beauty",
                "Merchandising",
                "Alternative Lenders",
                "Authentication Software",
                "B2B Payments",
                "BNPL",
                "Consumer FinTech",
                "Cross-Border Payments",
                "Digital Wallets",
                "Financial Management Software",
                "Infrastructure (FinTech)", 
                "Neo-banks",
                "Payment Processor / POS",
                "Government Tech",
                "FoodTech",
                "Grocery Tech", 
                "Packaging",
                "Real Estate / Mall Operators",
                "IoT",
                "Inventory Management",
                "Logistics & Supply Chain",
                "Mobility",
                "Leisure & Travel",
                "Marketplaces",
                "Travel & Leisure",
                "CRM",
                "CXP Platforms",
                "Event Management",
                "Experiential Players",
                "Loyalty",
                "MarTech",
                "Personalization Software",
                "Sales Enablement Software",
                "Cybersecurity",
                "Diversified / Others",
                "Financial Software",
                "Robotics & Drones",
                "InsurTech",
                "Media",
                "Product Information Management Software",
                "Print on Demand",
                "Gadgets",
                "Games / Sports / Toys", 
                "Recommerce",
                "Rental",
                "Beverages",
                "Catering",
                "Restaurant, Hospitality and Local Delivery Technology",
                "Ghost/Commercial Kitchens",
                "Restaurants",
                "Apparel",
                "E-commerce",
                "Luxury & Accessories",
                "Retailers",
                "Home Goods",
                "Data Analytics",
                "Data Management",
                "Retail Data",
                "Enterprise Search",
                "Social Platform / Software",
                "In-Store Technologies",
                "Robotics & Drones",
                "Software",
                "Professional Services",
                "HRTech",
                "Staffing",
                "Tech-enabled Services",
                "Workforce Management",
                "Telecommunications",
                "Ticketing and Events",
                "Trade Show Providers",
                "Utilities",
                "Utility and Energy Tech",
                "Web 3.0",
                "Gaming",
                "Data Integration",
                "Data Services",
                "Financial Institution", 
                "Financial Investors",
                "Corporate Venture Capital"
            ]

            description = {description}
            
            Example response = {{res: AdTech}}

            If you are unable to identify which cohort the company belongs to respond with "Not sure". Example = {{res: Not sure}}
        """
        
        # Create a prompt template which will be used to generate the prompt
        # It is specialised code from langchain which makes life easier
        self.prompt_template = PromptTemplate(
            input_variables=["description"],
            template=self.prompt_scaffold,
        )
        
        # Define the variable that holds the large language model
        self.llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)
        
    def classify(self, description: str) -> None:
        
        # Define langchain chain which will run the prompt
        chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
        
        # Result of the prompt after running it
        res = chain.run(description=description)
        
        return json.loads(res)["res"]
