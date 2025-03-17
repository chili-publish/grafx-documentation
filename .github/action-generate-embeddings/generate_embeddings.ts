import * as fs from 'fs';
import * as path from 'path';
import { OpenAI } from 'openai';
import * as dotenv from 'dotenv';
import { Embedding } from 'openai/resources';

dotenv.config();

const OPENAI_API_KEY = process.env.OPENAI_API_KEY;
if (!OPENAI_API_KEY) {
    throw new Error('OpenAI API key not found in environment variables.');
}

const configuration = {
    apiKey: OPENAI_API_KEY,
};
const openai = new OpenAI(configuration);

const EXTENSION = process.env.FILE_EXTENSION || '.md';
const CHUNK_SIZE = 100; // words
const INPUT_DIR = process.env.INPUT_DIR || process.cwd();
const OUTPUT_DIR = process.env.OUTPUT_DIR || path.join(process.cwd(), 'embeddings_output');

// Ensure output directory exists
if (!fs.existsSync(OUTPUT_DIR)) {
    console.log(`Creating output directory: ${OUTPUT_DIR}`);
    fs.mkdirSync(OUTPUT_DIR);
}

// Function to recursively get all files with the given extension
function getAllFiles(dir: string, extension: string, filesArray: string[] = []) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            getAllFiles(fullPath, extension, filesArray);
        } else if (path.extname(fullPath) === extension) {
            filesArray.push(fullPath);
        }
    }
    return filesArray;
}

// Function to split text into chunks of approximately CHUNK_SIZE words
function splitTextIntoChunks(text: string, chunkSize: number): string[] {
    const words = text.split(/\s+/);
    const chunks = [];
    for (let i = 0; i < words.length; i += chunkSize) {
        const chunk = words.slice(i, i + chunkSize).join(' ');
        chunks.push(chunk);
    }
    return chunks;
}

// Main function to process files
async function processFiles() {
    const files = getAllFiles(INPUT_DIR, EXTENSION);
    console.log(`Found ${files.length} '.${EXTENSION}' files.`);

    for (const filePath of files) {
        console.log(`Processing file: ${filePath}`);
        const text = fs.readFileSync(filePath, 'utf-8');
        const chunks = splitTextIntoChunks(text, CHUNK_SIZE);

        let embeddings :{
                chunk: string,
                embedding: Array<Embedding>
        }[] = [];
        const embeddingPromises = chunks.map(async (chunk) => {
            console.log(`Generating embedding for chunk: "${chunk.substring(0, 50)}..."`);
            try {
            const response = await openai.embeddings.create({
                model: 'text-embedding-3-large',
                input: chunk,
            });

            console.log(`Successfully generated embedding for chunk: "${chunk.substring(0, 50)}..."`);
            return {
                chunk,
                embedding: response.data,
            };
            } catch (error) {
            console.error(`Error generating embedding for chunk: ${error}`);
            return null;
            }
        });

        const results = await Promise.all(embeddingPromises);
        embeddings = results.filter(result => result !== null);

        // Write embeddings to JSON file
        const relativePath = path.relative(INPUT_DIR, filePath);
        const outputFilePath = path.join(OUTPUT_DIR, `${relativePath}.json`);

        // Ensure the directory exists
        const outputDir = path.dirname(outputFilePath);
        if (!fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        fs.writeFileSync(outputFilePath, JSON.stringify(embeddings, null, 2));
        console.log(`Embeddings written to: ${outputFilePath}`);
    }
}

processFiles().catch((error) => {
    console.error(`Error processing files: ${error}`);
    process.exit(1);
});