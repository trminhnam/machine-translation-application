import { Request, Response } from "express";

// https://bobbyhadz.com/blog/javascript-error-err-require-esm-of-es-module-node-fetch
import { RequestInfo, RequestInit } from "node-fetch";
const fetch = (url: RequestInfo, init?: RequestInit) =>
    import("node-fetch").then(({ default: fetch }) => fetch(url, init));

export const translate = async (req: Request, res: Response) => {
    const { source } = req.body;

    const body = {
        source: source,
    };

    const options = {
        hostname: process.env.TRANSLATE_HOST,
        path: process.env.TRANSLATE_PATH,
        method: "POST",
    };

    const response = await fetch(
        (process.env.TRANSLATE_HOST as string) + process.env.TRANSLATE_PATH,
        {
            method: "POST",
            body: JSON.stringify(body),
            headers: { "Content-Type": "application/json" },
        }
    );
    const data = (await response.json()) as { translation: string };

    res.status(200).json({
        translation: data.translation || "Hello World!",
    });

    // res.status(200).json({
    //     translation: "Hello World!",
    // });
};
