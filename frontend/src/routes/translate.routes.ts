import express from "express";

import { translate } from "../controllers/translate.controllers";

export const translateRouter = express.Router();

translateRouter.post("/", translate);
