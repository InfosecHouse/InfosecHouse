import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Open-Source',
    Svg: require('@site/static/img/globe.svg').default,
    description: (
      <>
        Anyone can contribute to Infosec House. Found a tool/resouce not mentioned? Feel free to submit PR on Github or reach us via social media.
      </>
    ),
  },
  {
    title: 'Manually Indexed',
    Svg: require('@site/static/img/storage.svg').default,
    description: (
      <>
        Infosec House was designed from the ground up. Every asset is manually added and never automated to provide quality over quantity experience.
      </>
    ),
  },
  {
    title: 'Education',
    Svg: require('@site/static/img/binarybrain.svg').default,
    description: (
      <>
        Learn the tools! Read our blogs and educate yourself on how to properly use the tools. Stop copying & pasting and learn the syntax.
      </>
    ),
  },

];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
