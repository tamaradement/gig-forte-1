

export const getDynamicUrl = () => {
  let url
  debugger;

  if (process.env.NODE_ENV === 'development') {
    
    url = "http://127.0.0.1:8000/tunes/tunes_api/";

  } else {
    
    url = "https://www.gigforte.com/tunes/tunes_api/";
  }

  return url
}