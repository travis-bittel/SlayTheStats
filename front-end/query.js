import { createRoot } from 'react-dom/client';
import QueryField from './QueryField';

const container = document.getElementById('query');
const root = createRoot(container);

root.render(<QueryField />);