export interface Book {
  id: string;
  title: string;
  author: string;
  outline: Chapter[];
}

export interface Chapter {
  id: string;
  title: string;
  content?: string;
  status: 'draft' | 'review' | 'completed';
}
