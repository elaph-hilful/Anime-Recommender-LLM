from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder 
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException


load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build the pipeline...") 

        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")

        processed_csv = loader.load_and_process()

        logger.info(f"Data loaded and processed, saved to {processed_csv}")


        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vector_store()

        logger.info("Vector store built and saved successfully.")

        logger.info("Pipeline build completed successfully.")
    except Exception as e:
        logger.error(f"Pipeline build failed: {str(e)}")
        raise CustomException("Error during pipeline build", e)
    
if __name__ == "__main__":
    main()