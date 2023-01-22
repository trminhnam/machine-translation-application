import path from "path";
import express, { Application, Request, Response } from "express";
import dotenv from "dotenv";

// Import Routes
import { translateRouter } from "./routes/translate.routes";

dotenv.config();

const app: Application = express();
const port = process.env.PORT || 3000;

// Body parsing Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Set static folder
app.use(express.static(path.join(__dirname, "/public")));

// Use Routes
app.use("/translate", translateRouter);

try {
    app.listen(port, (): void => {
        console.log(`⚡️[server] Server is running on port ${port}`);
        console.log(`⚡️[server] http://localhost:${port}`);
    });
} catch (error: any) {
    console.error(`Error occured: ${error.message}`);
}
