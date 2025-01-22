// place files you want to import through the `$lib` alias in this folder.

export const siteMetaData = {
    title: 'Beatcode',
    author: 'Shashank Rawat',
    headerTitle: 'theBoringGuy',
    email: 'shashank17nov@gmail.com',
    github: 'https://github.com/rawat-shashank',
    linkedin: 'https://www.linkedin.com/in/rawat-shashank',
    image: 'static/images/dp.png'
};

export const HEADER_NAV_LINKS = [
    { href: '/solutions', title: 'Solutions' },
    { href: '/topics', title: 'Topics' }
    //   { href: "/about", title: "About" },
];


if (process.env.NODE_ENV === 'dev') {
    HEADER_NAV_LINKS.push({ href: '/posts', title: 'Posts' });
}

export const isValidURL = (url: string): boolean => {
    try {
        new URL(url);
        return true;
    } catch (error) {
        return false;
    }
}
