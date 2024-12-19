export interface Post {
    id: number;
    title: string;
    subtitle?: string;
    content?: string;
    base64_image?: string;
}